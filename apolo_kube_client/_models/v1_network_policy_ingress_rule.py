from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_network_policy_peer import V1NetworkPolicyPeer
from .v1_network_policy_port import V1NetworkPolicyPort
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NetworkPolicyIngressRule",)


class V1NetworkPolicyIngressRule(BaseModel):
    from_: Annotated[
        list[V1NetworkPolicyPeer], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="from",
        validation_alias=AliasChoices("from_", "from"),
    )

    ports: Annotated[
        list[V1NetworkPolicyPort], BeforeValidator(_collection_if_none("[]"))
    ] = []
