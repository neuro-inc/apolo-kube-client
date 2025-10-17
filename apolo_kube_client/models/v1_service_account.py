from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference

__all__ = ("V1ServiceAccount",)


class V1ServiceAccount(BaseModel):
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

    image_pull_secrets: list[V1LocalObjectReference] = Field(
        default=[],
        serialization_alias="imagePullSecrets",
        validation_alias=AliasChoices("image_pull_secrets", "imagePullSecrets"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    secrets: list[V1ObjectReference] = Field(default=[])
