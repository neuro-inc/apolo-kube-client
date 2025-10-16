from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1PriorityClass",)


class V1PriorityClass(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    description: str | None = Field(default_factory=lambda: None, alias="description")

    global_default: bool | None = Field(
        default_factory=lambda: None, alias="globalDefault"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    preemption_policy: str | None = Field(
        default_factory=lambda: None, alias="preemptionPolicy"
    )

    value: int | None = Field(default_factory=lambda: None, alias="value")
