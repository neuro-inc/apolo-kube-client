from pydantic import BaseModel, Field

from .v1_network_policy_peer import V1NetworkPolicyPeer
from .v1_network_policy_port import V1NetworkPolicyPort


class V1NetworkPolicyIngressRule(BaseModel):
    _from: list[V1NetworkPolicyPeer] | None = Field(None, alias="from")

    ports: list[V1NetworkPolicyPort] | None = Field(None, alias="ports")
