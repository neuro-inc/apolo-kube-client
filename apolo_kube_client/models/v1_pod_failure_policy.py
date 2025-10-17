from pydantic import BaseModel
from .v1_pod_failure_policy_rule import V1PodFailurePolicyRule

__all__ = ("V1PodFailurePolicy",)


class V1PodFailurePolicy(BaseModel):
    rules: list[V1PodFailurePolicyRule] = []
