from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1NFSVolumeSource",)


class V1NFSVolumeSource(BaseModel):
    path: str | None = Field(None, alias="path")

    read_only: bool | None = Field(None, alias="readOnly")

    server: str | None = Field(None, alias="server")
