from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1GitRepoVolumeSource",)


class V1GitRepoVolumeSource(BaseModel):
    directory: str | None = Field(default_factory=lambda: None, alias="directory")

    repository: str | None = Field(default_factory=lambda: None, alias="repository")

    revision: str | None = Field(default_factory=lambda: None, alias="revision")
