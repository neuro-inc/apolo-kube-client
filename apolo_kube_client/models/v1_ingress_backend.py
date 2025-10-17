from pydantic import BaseModel, Field
from .v1_ingress_service_backend import V1IngressServiceBackend
from .v1_typed_local_object_reference import V1TypedLocalObjectReference

__all__ = ("V1IngressBackend",)


class V1IngressBackend(BaseModel):
    resource: V1TypedLocalObjectReference = Field(
        default_factory=lambda: V1TypedLocalObjectReference()
    )

    service: V1IngressServiceBackend = Field(
        default_factory=lambda: V1IngressServiceBackend()
    )
