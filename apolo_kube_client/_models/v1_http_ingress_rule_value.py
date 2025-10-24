from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_http_ingress_path import V1HTTPIngressPath

__all__ = ("V1HTTPIngressRuleValue",)


class V1HTTPIngressRuleValue(BaseModel):
    """HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.networking.v1.HTTPIngressRuleValue"
    )

    paths: Annotated[
        list[V1HTTPIngressPath],
        Field(
            description="""paths is a collection of paths that map requests to backends."""
        ),
    ]
