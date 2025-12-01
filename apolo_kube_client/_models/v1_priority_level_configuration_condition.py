from datetime import datetime
from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1PriorityLevelConfigurationCondition",)


class V1PriorityLevelConfigurationCondition(BaseConfiguredModel):
    """PriorityLevelConfigurationCondition defines the condition of priority level."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationCondition"
    )

    last_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastTransitionTime",
            description="""`lastTransitionTime` is the last time the condition transitioned from one status to another.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""`message` is a human-readable message indicating details about last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""`reason` is a unique, one-word, CamelCase reason for the condition's last transition.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        str | None,
        Field(
            description="""`status` is the status of the condition. Can be True, False, Unknown. Required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str | None,
        Field(
            description="""`type` is the type of the condition. Required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
