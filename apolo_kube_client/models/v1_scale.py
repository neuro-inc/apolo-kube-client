from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_scale_spec import V1ScaleSpec
from .v1_scale_status import V1ScaleStatus


class V1Scale(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1ScaleSpec | None = Field(None, alias="spec")

    status: V1ScaleStatus | None = Field(None, alias="status")
