from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1DeviceConstraint",)


class V1beta1DeviceConstraint(BaseModel):
    distinct_attribute: str | None = Field(
        default_factory=lambda: None, alias="distinctAttribute"
    )

    match_attribute: str | None = Field(
        default_factory=lambda: None, alias="matchAttribute"
    )

    requests: list[str] = Field(default_factory=lambda: [], alias="requests")
