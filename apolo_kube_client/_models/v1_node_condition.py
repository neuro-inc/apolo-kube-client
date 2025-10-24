from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1NodeCondition",)


class V1NodeCondition(BaseModel):
    """NodeCondition contains condition information for a node."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeCondition"

    last_heartbeat_time: Annotated[
        datetime | None,
        Field(
            alias="lastHeartbeatTime",
            description="""Last time we got an update on a given condition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    last_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastTransitionTime",
            description="""Last time the condition transit from one status to another.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""Human readable message indicating details about last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""(brief) reason for the condition's last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str,
        Field(description="""Status of the condition, one of True, False, Unknown."""),
    ]

    type: Annotated[str, Field(description="""Type of node condition.""")]
