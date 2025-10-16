from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha1_server_storage_version import V1alpha1ServerStorageVersion
from .v1alpha1_storage_version_condition import V1alpha1StorageVersionCondition

__all__ = ("V1alpha1StorageVersionStatus",)


class V1alpha1StorageVersionStatus(BaseModel):
    common_encoding_version: str | None = Field(
        default_factory=lambda: None, alias="commonEncodingVersion"
    )

    conditions: list[V1alpha1StorageVersionCondition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    storage_versions: list[V1alpha1ServerStorageVersion] = Field(
        default_factory=lambda: [], alias="storageVersions"
    )
