from pydantic import AliasChoices, BaseModel, Field
from .v1_ip_block import V1IPBlock
from .v1_label_selector import V1LabelSelector

__all__ = ("V1NetworkPolicyPeer",)


class V1NetworkPolicyPeer(BaseModel):
    ip_block: V1IPBlock = Field(
        default_factory=lambda: V1IPBlock(),
        serialization_alias="ipBlock",
        validation_alias=AliasChoices("ip_block", "ipBlock"),
    )

    namespace_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
    )

    pod_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="podSelector",
        validation_alias=AliasChoices("pod_selector", "podSelector"),
    )
