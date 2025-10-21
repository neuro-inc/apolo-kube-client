from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_network_policy_egress_rule import V1NetworkPolicyEgressRule
from .v1_network_policy_ingress_rule import V1NetworkPolicyIngressRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NetworkPolicySpec",)


class V1NetworkPolicySpec(BaseModel):
    egress: list[V1NetworkPolicyEgressRule] = []

    ingress: list[V1NetworkPolicyIngressRule] = []

    pod_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="podSelector",
        validation_alias=AliasChoices("pod_selector", "podSelector"),
    )

    policy_types: list[str] = Field(
        default=[],
        serialization_alias="policyTypes",
        validation_alias=AliasChoices("policy_types", "policyTypes"),
    )
