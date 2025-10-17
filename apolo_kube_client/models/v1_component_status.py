from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_component_condition import V1ComponentCondition
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1ComponentStatus",)


class V1ComponentStatus(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    conditions: list[V1ComponentCondition] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())
