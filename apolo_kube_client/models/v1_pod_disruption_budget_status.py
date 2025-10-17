from pydantic import AliasChoices, BaseModel, Field
from .v1_condition import V1Condition
from datetime import datetime

__all__ = ("V1PodDisruptionBudgetStatus",)


class V1PodDisruptionBudgetStatus(BaseModel):
    conditions: list[V1Condition] = []

    current_healthy: int | None = Field(
        default=None,
        serialization_alias="currentHealthy",
        validation_alias=AliasChoices("current_healthy", "currentHealthy"),
    )

    desired_healthy: int | None = Field(
        default=None,
        serialization_alias="desiredHealthy",
        validation_alias=AliasChoices("desired_healthy", "desiredHealthy"),
    )

    disrupted_pods: dict[str, datetime] = Field(
        default={},
        serialization_alias="disruptedPods",
        validation_alias=AliasChoices("disrupted_pods", "disruptedPods"),
    )

    disruptions_allowed: int | None = Field(
        default=None,
        serialization_alias="disruptionsAllowed",
        validation_alias=AliasChoices("disruptions_allowed", "disruptionsAllowed"),
    )

    expected_pods: int | None = Field(
        default=None,
        serialization_alias="expectedPods",
        validation_alias=AliasChoices("expected_pods", "expectedPods"),
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )
