from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1beta1DeviceConstraint",)


class V1beta1DeviceConstraint(BaseModel):
    distinct_attribute: str | None = Field(
        default=None,
        serialization_alias="distinctAttribute",
        validation_alias=AliasChoices("distinct_attribute", "distinctAttribute"),
    )

    match_attribute: str | None = Field(
        default=None,
        serialization_alias="matchAttribute",
        validation_alias=AliasChoices("match_attribute", "matchAttribute"),
    )

    requests: list[str] = Field(default=[])
