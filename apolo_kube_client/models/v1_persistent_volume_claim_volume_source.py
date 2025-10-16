from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1PersistentVolumeClaimVolumeSource",)


class V1PersistentVolumeClaimVolumeSource(BaseModel):
    claim_name: str | None = Field(None, alias="claimName")

    read_only: bool | None = Field(None, alias="readOnly")
