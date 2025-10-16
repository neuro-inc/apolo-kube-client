from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1NonResourceRule",)


class V1NonResourceRule(BaseModel):
    non_resource_ur_ls: list[str] | None = Field(None, alias="nonResourceURLs")

    verbs: list[str] | None = Field(None, alias="verbs")
