from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1Toleration",)


class V1Toleration(BaseModel):
    effect: str | None = Field(default=None)

    key: str | None = Field(default=None)

    operator: str | None = Field(default=None)

    toleration_seconds: int | None = Field(
        default=None,
        serialization_alias="tolerationSeconds",
        validation_alias=AliasChoices("toleration_seconds", "tolerationSeconds"),
    )

    value: str | None = Field(default=None)
