from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1SeccompProfile",)


class V1SeccompProfile(BaseModel):
    localhost_profile: str | None = Field(
        default=None,
        serialization_alias="localhostProfile",
        validation_alias=AliasChoices("localhost_profile", "localhostProfile"),
    )

    type: str | None = Field(default=None)
