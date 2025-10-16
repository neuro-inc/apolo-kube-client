from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1NodeFeatures",)


class V1NodeFeatures(BaseModel):
    supplemental_groups_policy: bool | None = Field(
        None, alias="supplementalGroupsPolicy"
    )
