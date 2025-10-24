from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_ingress_backend import V1IngressBackend

__all__ = ("V1HTTPIngressPath",)


class V1HTTPIngressPath(BaseModel):
    """HTTPIngressPath associates a path with a backend. Incoming urls matching the path are forwarded to the backend."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.HTTPIngressPath"

    backend: Annotated[
        V1IngressBackend,
        Field(
            description="""backend defines the referenced service endpoint to which the traffic will be forwarded to."""
        ),
    ]

    path: Annotated[
        str | None,
        Field(
            description="""path is matched against the path of an incoming request. Currently it can contain characters disallowed from the conventional "path" part of a URL as defined by RFC 3986. Paths must begin with a '/' and must be present when using PathType with value "Exact" or "Prefix".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    path_type: Annotated[
        str,
        Field(
            alias="pathType",
            description="""pathType determines the interpretation of the path matching. PathType can be one of the following values: * Exact: Matches the URL path exactly. * Prefix: Matches based on a URL path prefix split by '/'. Matching is
  done on a path element by element basis. A path element refers is the
  list of labels in the path split by the '/' separator. A request is a
  match for path p if every p is an element-wise prefix of p of the
  request path. Note that if the last element of the path is a substring
  of the last element in request path, it is not a match (e.g. /foo/bar
  matches /foo/bar/baz, but does not match /foo/barbaz).
* ImplementationSpecific: Interpretation of the Path matching is up to
  the IngressClass. Implementations can treat this as a separate PathType
  or treat it identically to Prefix or Exact path types.
Implementations are required to support all path types.""",
        ),
    ]
