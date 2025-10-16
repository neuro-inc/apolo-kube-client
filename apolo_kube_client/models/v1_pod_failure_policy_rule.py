from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_pod_failure_policy_on_exit_codes_requirement import (
    V1PodFailurePolicyOnExitCodesRequirement,
)
from .v1_pod_failure_policy_on_pod_conditions_pattern import (
    V1PodFailurePolicyOnPodConditionsPattern,
)

__all__ = ("V1PodFailurePolicyRule",)


class V1PodFailurePolicyRule(BaseModel):
    action: str | None = Field(default_factory=lambda: None, alias="action")

    on_exit_codes: V1PodFailurePolicyOnExitCodesRequirement = Field(
        default_factory=lambda: V1PodFailurePolicyOnExitCodesRequirement(),
        alias="onExitCodes",
    )

    on_pod_conditions: list[V1PodFailurePolicyOnPodConditionsPattern] = Field(
        default_factory=lambda: [], alias="onPodConditions"
    )
