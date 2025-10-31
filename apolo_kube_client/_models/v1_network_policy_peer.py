from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_ip_block import V1IPBlock
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator

__all__ = ("V1NetworkPolicyPeer",)


class V1NetworkPolicyPeer(BaseModel):
    """NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.NetworkPolicyPeer"

    ip_block: Annotated[
        V1IPBlock | None,
        Field(
            alias="ipBlock",
            description="""ipBlock defines policy on a particular IPBlock. If this field is set then neither of the other fields can be.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    namespace_selector: Annotated[
        V1LabelSelector,
        Field(
            alias="namespaceSelector",
            description="""namespaceSelector selects namespaces using cluster-scoped labels. This field follows standard label selector semantics; if present but empty, it selects all namespaces.

If podSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the namespaces selected by namespaceSelector. Otherwise it selects all pods in the namespaces selected by namespaceSelector.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LabelSelector)),
    ] = V1LabelSelector()

    pod_selector: Annotated[
        V1LabelSelector,
        Field(
            alias="podSelector",
            description="""podSelector is a label selector which selects pods. This field follows standard label selector semantics; if present but empty, it selects all pods.

If namespaceSelector is also set, then the NetworkPolicyPeer as a whole selects the pods matching podSelector in the Namespaces selected by NamespaceSelector. Otherwise it selects the pods matching podSelector in the policy's own namespace.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LabelSelector)),
    ] = V1LabelSelector()
