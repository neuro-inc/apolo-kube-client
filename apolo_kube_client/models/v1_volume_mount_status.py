from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1VolumeMountStatus",)


class V1VolumeMountStatus(BaseModel):
    mount_path: str | None = Field(None, alias="mountPath")

    name: str | None = Field(None, alias="name")

    read_only: bool | None = Field(None, alias="readOnly")

    recursive_read_only: str | None = Field(None, alias="recursiveReadOnly")
