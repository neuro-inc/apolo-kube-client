from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_http_header import V1HTTPHeader
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator

__all__ = ("V1HTTPGetAction",)


class V1HTTPGetAction(BaseModel):
    """HTTPGetAction describes an action based on HTTP Get requests."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.HTTPGetAction"

    host: Annotated[
        str | None,
        Field(
            description="""Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    http_headers: Annotated[
        list[V1HTTPHeader],
        Field(
            alias="httpHeaders",
            description="""Custom headers to set in the request. HTTP allows repeated headers.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    path: Annotated[
        str | None,
        Field(
            description="""Path to access on the HTTP server.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    port: Annotated[
        JsonType,
        Field(
            description="""Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME."""
        ),
    ]

    scheme: Annotated[
        str | None,
        Field(
            description="""Scheme to use for connecting to the host. Defaults to HTTP.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
