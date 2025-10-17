from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_toleration import V1Toleration

__all__ = ("V1Scheduling",)


class V1Scheduling(BaseModel):
    node_selector: dict[str, str] = Field(
        default={},
        serialization_alias="nodeSelector",
        validation_alias=AliasChoices("node_selector", "nodeSelector"),
    )

    tolerations: list[V1Toleration] = Field(default=[])
