from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1VolumeMountStatus",)


class V1VolumeMountStatus(BaseModel):
    mount_path: str | None = Field(default_factory=lambda: None, alias="mountPath")

    name: str | None = Field(default_factory=lambda: None)

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")

    recursive_read_only: str | None = Field(
        default_factory=lambda: None, alias="recursiveReadOnly"
    )
