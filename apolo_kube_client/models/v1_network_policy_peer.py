from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ip_block import V1IPBlock
from .v1_label_selector import V1LabelSelector

__all__ = ("V1NetworkPolicyPeer",)


class V1NetworkPolicyPeer(BaseModel):
    ip_block: V1IPBlock = Field(default_factory=lambda: V1IPBlock(), alias="ipBlock")

    namespace_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="namespaceSelector"
    )

    pod_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="podSelector"
    )
