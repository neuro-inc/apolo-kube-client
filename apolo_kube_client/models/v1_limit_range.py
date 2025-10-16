from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_limit_range_spec import V1LimitRangeSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1LimitRange",)


class V1LimitRange(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1LimitRangeSpec | None = Field(None, alias="spec")
