from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_pod_disruption_budget_spec import V1PodDisruptionBudgetSpec
from .v1_pod_disruption_budget_status import V1PodDisruptionBudgetStatus

__all__ = ("V1PodDisruptionBudget",)


class V1PodDisruptionBudget(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1PodDisruptionBudgetSpec = Field(
        default_factory=lambda: V1PodDisruptionBudgetSpec(), alias="spec"
    )

    status: V1PodDisruptionBudgetStatus = Field(
        default_factory=lambda: V1PodDisruptionBudgetStatus(), alias="status"
    )
