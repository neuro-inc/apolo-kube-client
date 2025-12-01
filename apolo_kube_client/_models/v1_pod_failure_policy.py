from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1_pod_failure_policy_rule import V1PodFailurePolicyRule


__all__ = ("V1PodFailurePolicy",)


class V1PodFailurePolicy(BaseConfiguredModel):
    """PodFailurePolicy describes how failed pods influence the backoffLimit."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.PodFailurePolicy"

    rules: Annotated[
        list[V1PodFailurePolicyRule],
        Field(
            description="""A list of pod failure policy rules. The rules are evaluated in order. Once a rule matches a Pod failure, the remaining of the rules are ignored. When no rule matches the Pod failure, the default handling applies - the counter of pod failures is incremented and it is checked against the backoffLimit. At most 20 elements are allowed."""
        ),
    ]
