from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_ingress_service_backend import V1IngressServiceBackend
from .v1_typed_local_object_reference import V1TypedLocalObjectReference

__all__ = ("V1IngressBackend",)


class V1IngressBackend(BaseModel):
    """IngressBackend describes all endpoints for a given service and port."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.IngressBackend"

    resource: Annotated[
        V1TypedLocalObjectReference | None,
        Field(
            description="""resource is an ObjectRef to another Kubernetes resource in the namespace of the Ingress object. If resource is specified, a service.Name and service.Port must not be specified. This is a mutually exclusive setting with "Service".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    service: Annotated[
        V1IngressServiceBackend | None,
        Field(
            description="""service references a service as a backend. This is a mutually exclusive setting with "Resource".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
