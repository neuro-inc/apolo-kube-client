from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1ResourcePool",)


class V1beta1ResourcePool(BaseModel):
    generation: int | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    resource_slice_count: int | None = Field(
        default_factory=lambda: None, alias="resourceSliceCount"
    )
