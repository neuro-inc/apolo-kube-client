from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ContainerRestartRuleOnExitCodes",)


class V1ContainerRestartRuleOnExitCodes(BaseModel):
    operator: str | None = Field(default=None)

    values: list[int] = Field(default=[])
