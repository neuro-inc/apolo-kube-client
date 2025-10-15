from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1beta1_i_p_address import V1beta1IPAddress


class V1beta1IPAddressList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1beta1IPAddress] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
