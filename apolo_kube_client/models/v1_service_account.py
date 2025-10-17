from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_local_object_reference import V1LocalObjectReference
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference

__all__ = ("V1ServiceAccount",)


class V1ServiceAccount(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    automount_service_account_token: bool | None = Field(
        default_factory=lambda: None, alias="automountServiceAccountToken"
    )

    image_pull_secrets: list[V1LocalObjectReference] = Field(
        default_factory=lambda: [], alias="imagePullSecrets"
    )

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    secrets: list[V1ObjectReference] = Field(default_factory=lambda: [])
