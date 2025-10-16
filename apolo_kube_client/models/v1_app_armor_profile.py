from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1AppArmorProfile",)


class V1AppArmorProfile(BaseModel):
    localhost_profile: str | None = Field(
        default_factory=lambda: None, alias="localhostProfile"
    )

    type: str | None = Field(default_factory=lambda: None, alias="type")
