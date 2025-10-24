from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_pod_failure_policy_rule import V1PodFailurePolicyRule

__all__ = ("V1PodFailurePolicy",)


class V1PodFailurePolicy(BaseModel):
    """PodFailurePolicy describes how failed pods influence the backoffLimit."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.PodFailurePolicy"

    rules: Annotated[
        list[V1PodFailurePolicyRule],
        Field(
            description="""A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed."""
        ),
    ]
