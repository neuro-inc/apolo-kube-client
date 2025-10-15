from datetime import datetime

from pydantic import BaseModel, Field

from .v1_condition import V1Condition


class V1PodDisruptionBudgetStatus(BaseModel):
    conditions: list[V1Condition] | None = Field(None, alias="conditions")

    current_healthy: int | None = Field(None, alias="currentHealthy")

    desired_healthy: int | None = Field(None, alias="desiredHealthy")

    disrupted_pods: dict(str, datetime) | None = Field(None, alias="disruptedPods")

    disruptions_allowed: int | None = Field(None, alias="disruptionsAllowed")

    expected_pods: int | None = Field(None, alias="expectedPods")

    observed_generation: int | None = Field(None, alias="observedGeneration")
