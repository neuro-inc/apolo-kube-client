from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_network_policy_peer import V1NetworkPolicyPeer
from .v1_network_policy_port import V1NetworkPolicyPort
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NetworkPolicyEgressRule",)


class V1NetworkPolicyEgressRule(BaseModel):
    ports: Annotated[
        list[V1NetworkPolicyPort], BeforeValidator(_collection_if_none("[]"))
    ] = []

    to: Annotated[
        list[V1NetworkPolicyPeer], BeforeValidator(_collection_if_none("[]"))
    ] = []
