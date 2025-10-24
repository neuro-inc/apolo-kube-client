from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ComponentCondition",)


class V1ComponentCondition(BaseModel):
    """Information about the condition of a component."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ComponentCondition"

    error: Annotated[
        str | None,
        Field(
            description="""Condition error code for a component. For example, a health check error code.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""Message about the condition for a component. For example, information about a health check.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str,
        Field(
            description="""Status of the condition for a component. Valid values for "Healthy": "True", "False", or "Unknown"."""
        ),
    ]

    type: Annotated[
        str,
        Field(
            description='''Type of condition for a component. Valid value: "Healthy"'''
        ),
    ]
