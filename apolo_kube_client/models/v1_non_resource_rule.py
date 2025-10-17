from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1NonResourceRule",)


class V1NonResourceRule(BaseModel):
    non_resource_ur_ls: list[str] = Field(
        default_factory=lambda: [], alias="nonResourceURLs"
    )

    verbs: list[str] = Field(default_factory=lambda: [])
