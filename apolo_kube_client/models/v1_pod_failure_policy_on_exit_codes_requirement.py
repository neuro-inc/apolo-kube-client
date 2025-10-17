from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1PodFailurePolicyOnExitCodesRequirement",)


class V1PodFailurePolicyOnExitCodesRequirement(BaseModel):
    container_name: str | None = Field(
        default=None,
        serialization_alias="containerName",
        validation_alias=AliasChoices("container_name", "containerName"),
    )

    operator: str | None = Field(default=None)

    values: list[int] = Field(default=[])
