from pydantic import AliasChoices, BaseModel, Field
from .v1_pod_failure_policy_on_exit_codes_requirement import (
    V1PodFailurePolicyOnExitCodesRequirement,
)
from .v1_pod_failure_policy_on_pod_conditions_pattern import (
    V1PodFailurePolicyOnPodConditionsPattern,
)

__all__ = ("V1PodFailurePolicyRule",)


class V1PodFailurePolicyRule(BaseModel):
    action: str | None = None

    on_exit_codes: V1PodFailurePolicyOnExitCodesRequirement = Field(
        default_factory=lambda: V1PodFailurePolicyOnExitCodesRequirement(),
        serialization_alias="onExitCodes",
        validation_alias=AliasChoices("on_exit_codes", "onExitCodes"),
    )

    on_pod_conditions: list[V1PodFailurePolicyOnPodConditionsPattern] = Field(
        default=[],
        serialization_alias="onPodConditions",
        validation_alias=AliasChoices("on_pod_conditions", "onPodConditions"),
    )
