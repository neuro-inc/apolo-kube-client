from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_service_backend_port import V1ServiceBackendPort
from pydantic import BeforeValidator

__all__ = ("V1IngressServiceBackend",)


class V1IngressServiceBackend(BaseModel):
    """IngressServiceBackend references a Kubernetes Service as a Backend."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.networking.v1.IngressServiceBackend"
    )

    name: Annotated[
        str,
        Field(
            description="""name is the referenced service. The service must exist in the same namespace as the Ingress object."""
        ),
    ]

    port: Annotated[
        V1ServiceBackendPort,
        Field(
            description="""port of the referenced service. A port name or port number is required for a IngressServiceBackend.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ServiceBackendPort)),
    ] = V1ServiceBackendPort()
