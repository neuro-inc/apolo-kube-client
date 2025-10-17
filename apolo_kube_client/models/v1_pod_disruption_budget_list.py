from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_pod_disruption_budget import V1PodDisruptionBudget

__all__ = ("V1PodDisruptionBudgetList",)


class V1PodDisruptionBudgetList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1PodDisruptionBudget] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
