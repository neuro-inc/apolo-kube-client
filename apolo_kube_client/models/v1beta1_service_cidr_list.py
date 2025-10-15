from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1beta1_service_c_i_d_r import V1beta1ServiceCIDR


class V1beta1ServiceCIDRList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1beta1ServiceCIDR] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
