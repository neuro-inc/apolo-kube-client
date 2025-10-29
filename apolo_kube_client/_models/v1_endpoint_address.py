from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator

__all__ = ("V1EndpointAddress",)


class V1EndpointAddress(BaseModel):
    """EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EndpointAddress"

    hostname: Annotated[
        str | None,
        Field(
            description="""The Hostname of this endpoint""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ip: Annotated[
        str,
        Field(
            description="""The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16)."""
        ),
    ]

    node_name: Annotated[
        str | None,
        Field(
            alias="nodeName",
            description="""Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    target_ref: Annotated[
        V1ObjectReference,
        Field(
            alias="targetRef",
            description="""Reference to object providing the endpoint.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectReference)),
    ] = V1ObjectReference()
