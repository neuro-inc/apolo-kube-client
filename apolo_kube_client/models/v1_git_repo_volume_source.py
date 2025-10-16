from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1GitRepoVolumeSource",)


class V1GitRepoVolumeSource(BaseModel):
    directory: str | None = Field(None, alias="directory")

    repository: str | None = Field(None, alias="repository")

    revision: str | None = Field(None, alias="revision")
