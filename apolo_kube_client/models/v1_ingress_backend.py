from pydantic import BaseModel, Field

from .v1_ingress_service_backend import V1IngressServiceBackend
from .v1_typed_local_object_reference import V1TypedLocalObjectReference


class V1IngressBackend(BaseModel):
    resource: V1TypedLocalObjectReference | None = Field(None, alias="resource")

    service: V1IngressServiceBackend | None = Field(None, alias="service")
