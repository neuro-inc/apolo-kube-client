from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1beta1DeviceAttribute",)


class V1beta1DeviceAttribute(BaseModel):
    bool: bool | None = Field(None, alias="bool")

    int: int | None = Field(None, alias="int")

    string: str | None = Field(None, alias="string")

    version: str | None = Field(None, alias="version")
