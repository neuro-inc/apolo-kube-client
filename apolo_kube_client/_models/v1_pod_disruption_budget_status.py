from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_condition import V1Condition
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodDisruptionBudgetStatus",)


class V1PodDisruptionBudgetStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    current_healthy: int | None = Field(
        default=None,
        serialization_alias="currentHealthy",
        validation_alias=AliasChoices("current_healthy", "currentHealthy"),
        exclude_if=_exclude_if,
    )

    desired_healthy: int | None = Field(
        default=None,
        serialization_alias="desiredHealthy",
        validation_alias=AliasChoices("desired_healthy", "desiredHealthy"),
        exclude_if=_exclude_if,
    )

    disrupted_pods: Annotated[
        dict[str, datetime], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="disruptedPods",
        validation_alias=AliasChoices("disrupted_pods", "disruptedPods"),
        exclude_if=_exclude_if,
    )

    disruptions_allowed: int | None = Field(
        default=None,
        serialization_alias="disruptionsAllowed",
        validation_alias=AliasChoices("disruptions_allowed", "disruptionsAllowed"),
        exclude_if=_exclude_if,
    )

    expected_pods: int | None = Field(
        default=None,
        serialization_alias="expectedPods",
        validation_alias=AliasChoices("expected_pods", "expectedPods"),
        exclude_if=_exclude_if,
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
        exclude_if=_exclude_if,
    )
