from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1beta1_resource_slice_spec import V1beta1ResourceSliceSpec


class V1beta1ResourceSlice(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1beta1ResourceSliceSpec | None = Field(None, alias="spec")
