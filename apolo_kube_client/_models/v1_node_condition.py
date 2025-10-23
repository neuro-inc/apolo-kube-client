from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1NodeCondition",)


class V1NodeCondition(BaseModel):
    last_heartbeat_time: datetime | None = Field(
        default=None,
        serialization_alias="lastHeartbeatTime",
        validation_alias=AliasChoices("last_heartbeat_time", "lastHeartbeatTime"),
        exclude_if=_exclude_if,
    )

    last_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastTransitionTime",
        validation_alias=AliasChoices("last_transition_time", "lastTransitionTime"),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    status: str | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
