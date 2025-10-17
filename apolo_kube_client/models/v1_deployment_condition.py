from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1DeploymentCondition",)


class V1DeploymentCondition(BaseModel):
    last_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastTransitionTime",
        validation_alias=AliasChoices("last_transition_time", "lastTransitionTime"),
    )

    last_update_time: datetime | None = Field(
        default=None,
        serialization_alias="lastUpdateTime",
        validation_alias=AliasChoices("last_update_time", "lastUpdateTime"),
    )

    message: str | None = Field(default=None)

    reason: str | None = Field(default=None)

    status: str | None = Field(default=None)

    type: str | None = Field(default=None)
