from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PersistentVolumeClaimVolumeSource",)


class V1PersistentVolumeClaimVolumeSource(BaseModel):
    claim_name: str | None = Field(default_factory=lambda: None, alias="claimName")

    read_only: bool | None = Field(default_factory=lambda: None, alias="readOnly")
