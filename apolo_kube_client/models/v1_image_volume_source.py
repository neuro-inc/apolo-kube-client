from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ImageVolumeSource",)


class V1ImageVolumeSource(BaseModel):
    pull_policy: str | None = Field(None, alias="pullPolicy")

    reference: str | None = Field(None, alias="reference")
