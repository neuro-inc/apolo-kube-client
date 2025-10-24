from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1BoundObjectReference",)


class V1BoundObjectReference(BaseModel):
    """BoundObjectReference is a reference to an object that a token is bound to."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authentication.v1.BoundObjectReference"
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""API version of the referent.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str | None,
        Field(
            description="""Kind of the referent. Valid kinds are 'Pod' and 'Secret'.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str | None,
        Field(description="""Name of the referent.""", exclude_if=lambda v: v is None),
    ] = None

    uid: Annotated[
        str | None,
        Field(description="""UID of the referent.""", exclude_if=lambda v: v is None),
    ] = None
