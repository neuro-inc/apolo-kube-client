from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_pod_failure_policy_on_exit_codes_requirement import (
    V1PodFailurePolicyOnExitCodesRequirement,
)
from .v1_pod_failure_policy_on_pod_conditions_pattern import (
    V1PodFailurePolicyOnPodConditionsPattern,
)
from pydantic import BeforeValidator

__all__ = ("V1PodFailurePolicyRule",)


class V1PodFailurePolicyRule(BaseModel):
    """PodFailurePolicyRule describes how a pod failure is handled when the requirements are met. One of onExitCodes and onPodConditions, but not both, can be used in each rule."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.PodFailurePolicyRule"

    action: Annotated[
        str,
        Field(
            description="""Specifies the action taken on a pod failure when the requirements are satisfied. Possible values are:

- FailJob: indicates that the pod's job is marked as Failed and all
  running pods are terminated.
- FailIndex: indicates that the pod's index is marked as Failed and will
  not be restarted.
- Ignore: indicates that the counter towards the .backoffLimit is not
  incremented and a replacement pod is created.
- Count: indicates that the pod is handled in the default way - the
  counter towards the .backoffLimit is incremented.
Additional values are considered to be added in the future. Clients should react to an unknown action by skipping the rule."""
        ),
    ]

    on_exit_codes: Annotated[
        V1PodFailurePolicyOnExitCodesRequirement | None,
        Field(
            alias="onExitCodes",
            description="""Represents the requirement on the container exit codes.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    on_pod_conditions: Annotated[
        list[V1PodFailurePolicyOnPodConditionsPattern],
        Field(
            alias="onPodConditions",
            description="""Represents the requirement on the pod conditions. The requirement is represented as a list of pod condition patterns. The requirement is satisfied if at least one pattern matches an actual pod condition. At most 20 elements are allowed.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
