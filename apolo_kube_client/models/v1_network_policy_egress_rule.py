from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_network_policy_peer import V1NetworkPolicyPeer
from .v1_network_policy_port import V1NetworkPolicyPort

__all__ = ("V1NetworkPolicyEgressRule",)


class V1NetworkPolicyEgressRule(BaseModel):
    ports: list[V1NetworkPolicyPort] | None = Field(None, alias="ports")

    to: list[V1NetworkPolicyPeer] | None = Field(None, alias="to")
