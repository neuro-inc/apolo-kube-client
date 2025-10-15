from pydantic import BaseModel, Field

from .v1_i_p_block import V1IPBlock
from .v1_label_selector import V1LabelSelector


class V1NetworkPolicyPeer(BaseModel):
    ip_block: V1IPBlock | None = Field(None, alias="ipBlock")

    namespace_selector: V1LabelSelector | None = Field(None, alias="namespaceSelector")

    pod_selector: V1LabelSelector | None = Field(None, alias="podSelector")
