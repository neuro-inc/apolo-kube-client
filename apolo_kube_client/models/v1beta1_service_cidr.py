from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1beta1_service_c_i_d_r_spec import V1beta1ServiceCIDRSpec
from .v1beta1_service_c_i_d_r_status import V1beta1ServiceCIDRStatus


class V1beta1ServiceCIDR(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1beta1ServiceCIDRSpec | None = Field(None, alias="spec")

    status: V1beta1ServiceCIDRStatus | None = Field(None, alias="status")
