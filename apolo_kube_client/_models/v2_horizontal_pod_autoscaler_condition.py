from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V2HorizontalPodAutoscalerCondition",)


class V2HorizontalPodAutoscalerCondition(BaseModel):
    """HorizontalPodAutoscalerCondition describes the state of a HorizontalPodAutoscaler at a certain point."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerCondition"
    )

    last_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastTransitionTime",
            description="""lastTransitionTime is the last time the condition transitioned from one status to another""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""message is a human-readable explanation containing details about the transition""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""reason is the reason for the condition's last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str,
        Field(
            description="""status is the status of the condition (True, False, Unknown)"""
        ),
    ]

    type: Annotated[str, Field(description="""type describes the current condition""")]
