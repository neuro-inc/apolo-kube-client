from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1DaemonSetCondition",)


class V1DaemonSetCondition(BaseModel):
    """DaemonSetCondition describes the state of a DaemonSet at a certain point."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DaemonSetCondition"

    last_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastTransitionTime",
            description="""Last time the condition transitioned from one status to another.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""A human readable message indicating details about the transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""The reason for the condition's last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str,
        Field(description="""Status of the condition, one of True, False, Unknown."""),
    ]

    type: Annotated[str, Field(description="""Type of DaemonSet condition.""")]
