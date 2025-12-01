from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _default_if_none
from .v1_service_backend_port import V1ServiceBackendPort


__all__ = ("V1IngressServiceBackend",)


class V1IngressServiceBackend(BaseConfiguredModel):
    """IngressServiceBackend references a Kubernetes Service as a Backend."""

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
