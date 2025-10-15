from pydantic import BaseModel, Field

from .v1_pod_failure_policy_rule import V1PodFailurePolicyRule


class V1PodFailurePolicy(BaseModel):
    rules: list[V1PodFailurePolicyRule] | None = Field(None, alias="rules")
