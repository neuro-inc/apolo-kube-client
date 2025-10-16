from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1SeccompProfile",)


class V1SeccompProfile(BaseModel):
    localhost_profile: str | None = Field(None, alias="localhostProfile")

    type: str | None = Field(None, alias="type")
