from datetime import datetime

from pydantic import BaseModel, Field


class V1CustomResourceDefinitionCondition(BaseModel):
    last_transition_time: datetime | None = Field(None, alias="lastTransitionTime")

    message: str | None = Field(None, alias="message")

    reason: str | None = Field(None, alias="reason")

    status: str | None = Field(None, alias="status")

    type: str | None = Field(None, alias="type")
