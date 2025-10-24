from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("CoreV1EndpointPort",)


class CoreV1EndpointPort(BaseModel):
    """EndpointPort is a tuple that describes a single port. Deprecated: This API is deprecated in v1.33+."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EndpointPort"

    app_protocol: Annotated[
        str | None,
        Field(
            alias="appProtocol",
            description="""The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:

* Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).

* Kubernetes-defined prefixed names:
  * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
  * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
  * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455

* Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str | None,
        Field(
            description="""The name of this port.  This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[int, Field(description="""The port number of the endpoint.""")]

    protocol: Annotated[
        str | None,
        Field(
            description="""The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
