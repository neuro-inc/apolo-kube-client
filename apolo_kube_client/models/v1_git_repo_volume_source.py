from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1GitRepoVolumeSource",)


class V1GitRepoVolumeSource(BaseModel):
    directory: str | None = Field(default=None)

    repository: str | None = Field(default=None)

    revision: str | None = Field(default=None)
