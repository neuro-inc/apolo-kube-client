from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1PriorityClass",)


class V1PriorityClass(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    description: str | None = Field(default=None)

    global_default: bool | None = Field(
        default=None,
        serialization_alias="globalDefault",
        validation_alias=AliasChoices("global_default", "globalDefault"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    preemption_policy: str | None = Field(
        default=None,
        serialization_alias="preemptionPolicy",
        validation_alias=AliasChoices("preemption_policy", "preemptionPolicy"),
    )

    value: int | None = Field(default=None)
