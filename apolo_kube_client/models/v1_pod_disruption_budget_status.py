from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_condition import V1Condition
from datetime import datetime

__all__ = ("V1PodDisruptionBudgetStatus",)


class V1PodDisruptionBudgetStatus(BaseModel):
    conditions: list[V1Condition] = Field(
        default_factory=lambda: [], alias="conditions"
    )

    current_healthy: int | None = Field(
        default_factory=lambda: None, alias="currentHealthy"
    )

    desired_healthy: int | None = Field(
        default_factory=lambda: None, alias="desiredHealthy"
    )

    disrupted_pods: dict[str, datetime] = Field(
        default_factory=lambda: {}, alias="disruptedPods"
    )

    disruptions_allowed: int | None = Field(
        default_factory=lambda: None, alias="disruptionsAllowed"
    )

    expected_pods: int | None = Field(
        default_factory=lambda: None, alias="expectedPods"
    )

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )
