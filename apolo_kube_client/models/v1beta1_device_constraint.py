from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1beta1DeviceConstraint",)


class V1beta1DeviceConstraint(BaseModel):
    match_attribute: str | None = Field(None, alias="matchAttribute")

    requests: list[str] | None = Field(None, alias="requests")
