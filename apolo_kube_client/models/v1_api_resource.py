from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1APIResource",)


class V1APIResource(BaseModel):
    categories: list[str] | None = Field(None, alias="categories")

    group: str | None = Field(None, alias="group")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    namespaced: bool | None = Field(None, alias="namespaced")

    short_names: list[str] | None = Field(None, alias="shortNames")

    singular_name: str | None = Field(None, alias="singularName")

    storage_version_hash: str | None = Field(None, alias="storageVersionHash")

    verbs: list[str] | None = Field(None, alias="verbs")

    version: str | None = Field(None, alias="version")
