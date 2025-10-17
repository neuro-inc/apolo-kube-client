from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1alpha1ServerStorageVersion",)


class V1alpha1ServerStorageVersion(BaseModel):
    api_server_id: str | None = Field(default_factory=lambda: None, alias="apiServerID")

    decodable_versions: list[str] = Field(
        default_factory=lambda: [], alias="decodableVersions"
    )

    encoding_version: str | None = Field(
        default_factory=lambda: None, alias="encodingVersion"
    )

    served_versions: list[str] = Field(
        default_factory=lambda: [], alias="servedVersions"
    )
