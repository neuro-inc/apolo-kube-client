from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1PodFailurePolicyOnExitCodesRequirement",)


class V1PodFailurePolicyOnExitCodesRequirement(BaseModel):
    container_name: str | None = Field(None, alias="containerName")

    operator: str | None = Field(None, alias="operator")

    values: list[int] | None = Field(None, alias="values")
