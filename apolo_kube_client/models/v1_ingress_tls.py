from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1IngressTLS",)


class V1IngressTLS(BaseModel):
    hosts: list[str] = Field(default=[])

    secret_name: str | None = Field(
        default=None,
        serialization_alias="secretName",
        validation_alias=AliasChoices("secret_name", "secretName"),
    )
