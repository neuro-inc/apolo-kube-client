from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1Overhead",)


class V1Overhead(BaseModel):
    pod_fixed: dict[str, str] = Field(
        default={},
        serialization_alias="podFixed",
        validation_alias=AliasChoices("pod_fixed", "podFixed"),
    )
