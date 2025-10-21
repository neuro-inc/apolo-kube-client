from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_status import V1alpha1StorageVersionStatus
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1StorageVersion",)


class V1alpha1StorageVersion(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: JsonType = {}

    status: Annotated[
        V1alpha1StorageVersionStatus,
        BeforeValidator(_default_if_none(V1alpha1StorageVersionStatus)),
    ] = Field(default_factory=lambda: V1alpha1StorageVersionStatus())
