from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_status import V1alpha1StorageVersionStatus
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1alpha1StorageVersion",)


class V1alpha1StorageVersion(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: JsonType = Field(default_factory=lambda: {})

    status: V1alpha1StorageVersionStatus = Field(
        default_factory=lambda: V1alpha1StorageVersionStatus()
    )
