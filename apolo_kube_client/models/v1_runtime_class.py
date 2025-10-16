from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_overhead import V1Overhead
from .v1_scheduling import V1Scheduling

__all__ = ("V1RuntimeClass",)


class V1RuntimeClass(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    handler: str | None = Field(default_factory=lambda: None, alias="handler")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    overhead: V1Overhead = Field(default_factory=lambda: V1Overhead(), alias="overhead")

    scheduling: V1Scheduling = Field(
        default_factory=lambda: V1Scheduling(), alias="scheduling"
    )
