from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_component_condition import V1ComponentCondition
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1ComponentStatus",)


class V1ComponentStatus(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    conditions: list[V1ComponentCondition] | None = Field(None, alias="conditions")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")
