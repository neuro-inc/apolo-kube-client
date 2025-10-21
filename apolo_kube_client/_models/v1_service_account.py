from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_local_object_reference import V1LocalObjectReference
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ServiceAccount",)


class V1ServiceAccount(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    automount_service_account_token: bool | None = Field(
        default=None,
        serialization_alias="automountServiceAccountToken",
        validation_alias=AliasChoices(
            "automount_service_account_token", "automountServiceAccountToken"
        ),
    )

    image_pull_secrets: Annotated[
        list[V1LocalObjectReference], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="imagePullSecrets",
        validation_alias=AliasChoices("image_pull_secrets", "imagePullSecrets"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    secrets: Annotated[
        list[V1ObjectReference], BeforeValidator(_collection_if_none("[]"))
    ] = []
