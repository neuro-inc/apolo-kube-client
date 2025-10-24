from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1IngressClassParametersReference",)


class V1IngressClassParametersReference(BaseModel):
    """IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.networking.v1.IngressClassParametersReference"
    )

    api_group: Annotated[
        str | None,
        Field(
            alias="apiGroup",
            description="""apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str, Field(description="""kind is the type of resource being referenced.""")
    ]

    name: Annotated[
        str, Field(description="""name is the name of resource being referenced.""")
    ]

    namespace: Annotated[
        str | None,
        Field(
            description="""namespace is the namespace of the resource being referenced. This field is required when scope is set to "Namespace" and must be unset when scope is set to "Cluster".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    scope: Annotated[
        str | None,
        Field(
            description="""scope represents if this refers to a cluster or namespace scoped resource. This may be set to "Cluster" (default) or "Namespace".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
