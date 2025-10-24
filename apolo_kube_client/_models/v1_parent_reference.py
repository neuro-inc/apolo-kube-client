from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ParentReference",)


class V1ParentReference(BaseModel):
    """ParentReference describes a reference to a parent object."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.ParentReference"

    group: Annotated[
        str | None,
        Field(
            description="""Group is the group of the object being referenced.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str, Field(description="""Name is the name of the object being referenced.""")
    ]

    namespace: Annotated[
        str | None,
        Field(
            description="""Namespace is the namespace of the object being referenced.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource: Annotated[
        str,
        Field(
            description="""Resource is the resource of the object being referenced."""
        ),
    ]
