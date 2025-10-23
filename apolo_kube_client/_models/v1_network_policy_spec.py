from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_label_selector import V1LabelSelector
from .v1_network_policy_egress_rule import V1NetworkPolicyEgressRule
from .v1_network_policy_ingress_rule import V1NetworkPolicyIngressRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NetworkPolicySpec",)


class V1NetworkPolicySpec(BaseModel):
    egress: Annotated[
        list[V1NetworkPolicyEgressRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    ingress: Annotated[
        list[V1NetworkPolicyIngressRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    pod_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="podSelector",
        validation_alias=AliasChoices("pod_selector", "podSelector"),
        exclude_if=_exclude_if,
    )

    policy_types: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="policyTypes",
            validation_alias=AliasChoices("policy_types", "policyTypes"),
            exclude_if=_exclude_if,
        )
    )
