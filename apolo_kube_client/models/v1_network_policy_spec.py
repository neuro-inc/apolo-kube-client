from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_network_policy_egress_rule import V1NetworkPolicyEgressRule
from .v1_network_policy_ingress_rule import V1NetworkPolicyIngressRule

__all__ = ("V1NetworkPolicySpec",)


class V1NetworkPolicySpec(BaseModel):
    egress: list[V1NetworkPolicyEgressRule] = Field(default_factory=lambda: [])

    ingress: list[V1NetworkPolicyIngressRule] = Field(default_factory=lambda: [])

    pod_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="podSelector"
    )

    policy_types: list[str] = Field(default_factory=lambda: [], alias="policyTypes")
