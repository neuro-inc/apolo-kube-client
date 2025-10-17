from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ResourceFieldSelector",)


class V1ResourceFieldSelector(BaseModel):
    container_name: str | None = Field(
        default_factory=lambda: None, alias="containerName"
    )

    divisor: str | None = Field(default_factory=lambda: None)

    resource: str | None = Field(default_factory=lambda: None)
