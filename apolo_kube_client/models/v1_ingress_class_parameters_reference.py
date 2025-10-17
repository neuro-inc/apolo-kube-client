from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1IngressClassParametersReference",)


class V1IngressClassParametersReference(BaseModel):
    api_group: str | None = Field(
        default=None,
        serialization_alias="apiGroup",
        validation_alias=AliasChoices("api_group", "apiGroup"),
    )

    kind: str | None = Field(default=None)

    name: str | None = Field(default=None)

    namespace: str | None = Field(default=None)

    scope: str | None = Field(default=None)
