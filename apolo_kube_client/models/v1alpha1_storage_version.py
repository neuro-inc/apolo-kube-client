from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_status import V1alpha1StorageVersionStatus

__all__ = ("V1alpha1StorageVersion",)


class V1alpha1StorageVersion(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: JsonType | None = Field(None, alias="spec")

    status: V1alpha1StorageVersionStatus | None = Field(None, alias="status")
