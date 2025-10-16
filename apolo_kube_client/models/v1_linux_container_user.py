from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1LinuxContainerUser",)


class V1LinuxContainerUser(BaseModel):
    gid: int | None = Field(None, alias="gid")

    supplemental_groups: list[int] | None = Field(None, alias="supplementalGroups")

    uid: int | None = Field(None, alias="uid")
