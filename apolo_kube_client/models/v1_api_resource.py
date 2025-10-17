from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1APIResource",)


class V1APIResource(BaseModel):
    categories: list[str] = Field(default_factory=lambda: [])

    group: str | None = Field(default_factory=lambda: None)

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    namespaced: bool | None = Field(default_factory=lambda: None)

    short_names: list[str] = Field(default_factory=lambda: [], alias="shortNames")

    singular_name: str | None = Field(
        default_factory=lambda: None, alias="singularName"
    )

    storage_version_hash: str | None = Field(
        default_factory=lambda: None, alias="storageVersionHash"
    )

    verbs: list[str] = Field(default_factory=lambda: [])

    version: str | None = Field(default_factory=lambda: None)
