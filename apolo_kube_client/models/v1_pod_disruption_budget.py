from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_pod_disruption_budget_spec import V1PodDisruptionBudgetSpec
from .v1_pod_disruption_budget_status import V1PodDisruptionBudgetStatus

__all__ = ("V1PodDisruptionBudget",)


class V1PodDisruptionBudget(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1PodDisruptionBudgetSpec | None = Field(None, alias="spec")

    status: V1PodDisruptionBudgetStatus | None = Field(None, alias="status")
