from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_ip_block import V1IPBlock
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NetworkPolicyPeer",)


class V1NetworkPolicyPeer(BaseModel):
    ip_block: Annotated[V1IPBlock, BeforeValidator(_default_if_none(V1IPBlock))] = (
        Field(
            default_factory=lambda: V1IPBlock(),
            serialization_alias="ipBlock",
            validation_alias=AliasChoices("ip_block", "ipBlock"),
            exclude_if=_exclude_if,
        )
    )

    namespace_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
        exclude_if=_exclude_if,
    )

    pod_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="podSelector",
        validation_alias=AliasChoices("pod_selector", "podSelector"),
        exclude_if=_exclude_if,
    )
