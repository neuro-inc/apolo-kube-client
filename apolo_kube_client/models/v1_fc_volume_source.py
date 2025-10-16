from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1FCVolumeSource",)


class V1FCVolumeSource(BaseModel):
    fs_type: str | None = Field(None, alias="fsType")

    lun: int | None = Field(None, alias="lun")

    read_only: bool | None = Field(None, alias="readOnly")

    target_ww_ns: list[str] | None = Field(None, alias="targetWWNs")

    wwids: list[str] | None = Field(None, alias="wwids")
