from pydantic import BaseModel, Field

from .v1_c_s_i_driver_spec import V1CSIDriverSpec
from .v1_object_meta import V1ObjectMeta


class V1CSIDriver(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1CSIDriverSpec | None = Field(None, alias="spec")
