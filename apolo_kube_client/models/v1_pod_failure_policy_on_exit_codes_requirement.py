from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodFailurePolicyOnExitCodesRequirement",)


class V1PodFailurePolicyOnExitCodesRequirement(BaseModel):
    container_name: str | None = Field(
        default_factory=lambda: None, alias="containerName"
    )

    operator: str | None = Field(default_factory=lambda: None, alias="operator")

    values: list[int] = Field(default_factory=lambda: [], alias="values")
