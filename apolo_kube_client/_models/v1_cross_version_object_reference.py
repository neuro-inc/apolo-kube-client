from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1CrossVersionObjectReference",)


class V1CrossVersionObjectReference(BaseModel):
    """CrossVersionObjectReference contains enough information to let you identify the referred resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v1.CrossVersionObjectReference"
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""apiVersion is the API version of the referent""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str,
        Field(
            description="""kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names"""
        ),
    ]
