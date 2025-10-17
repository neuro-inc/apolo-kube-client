from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ResourceFieldSelector",)


class V1ResourceFieldSelector(BaseModel):
    container_name: str | None = Field(
        default=None,
        serialization_alias="containerName",
        validation_alias=AliasChoices("container_name", "containerName"),
    )

    divisor: str | None = Field(default=None)

    resource: str | None = Field(default=None)
