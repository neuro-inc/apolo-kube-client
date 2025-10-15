from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1alpha3_device_class_spec import V1alpha3DeviceClassSpec


class V1alpha3DeviceClass(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1alpha3DeviceClassSpec | None = Field(None, alias="spec")
