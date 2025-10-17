from pydantic import AliasChoices, BaseModel, Field
from .v1_network_policy_peer import V1NetworkPolicyPeer
from .v1_network_policy_port import V1NetworkPolicyPort

__all__ = ("V1NetworkPolicyIngressRule",)


class V1NetworkPolicyIngressRule(BaseModel):
    from_: list[V1NetworkPolicyPeer] = Field(
        default=[],
        serialization_alias="from",
        validation_alias=AliasChoices("from_", "from"),
    )

    ports: list[V1NetworkPolicyPort] = []
