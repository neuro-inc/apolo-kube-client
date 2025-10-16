from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_limit_range_spec import V1LimitRangeSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1LimitRange",)


class V1LimitRange(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1LimitRangeSpec = Field(
        default_factory=lambda: V1LimitRangeSpec(), alias="spec"
    )
