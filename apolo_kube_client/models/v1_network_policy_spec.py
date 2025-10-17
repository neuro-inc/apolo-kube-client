from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_network_policy_egress_rule import V1NetworkPolicyEgressRule
from .v1_network_policy_ingress_rule import V1NetworkPolicyIngressRule

__all__ = ("V1NetworkPolicySpec",)


class V1NetworkPolicySpec(BaseModel):
    egress: list[V1NetworkPolicyEgressRule] = Field(default=[])

    ingress: list[V1NetworkPolicyIngressRule] = Field(default=[])

    pod_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="podSelector",
        validation_alias=AliasChoices("pod_selector", "podSelector"),
    )

    policy_types: list[str] = Field(
        default=[],
        serialization_alias="policyTypes",
        validation_alias=AliasChoices("policy_types", "policyTypes"),
    )
