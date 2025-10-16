from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1LinuxContainerUser",)


class V1LinuxContainerUser(BaseModel):
    gid: int | None = Field(default_factory=lambda: None, alias="gid")

    supplemental_groups: list[int] = Field(
        default_factory=lambda: [], alias="supplementalGroups"
    )

    uid: int | None = Field(default_factory=lambda: None, alias="uid")
