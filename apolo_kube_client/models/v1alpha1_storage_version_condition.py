from datetime import datetime

from pydantic import BaseModel, Field


class V1alpha1StorageVersionCondition(BaseModel):
    last_transition_time: datetime | None = Field(None, alias="lastTransitionTime")

    message: str | None = Field(None, alias="message")

    observed_generation: int | None = Field(None, alias="observedGeneration")

    reason: str | None = Field(None, alias="reason")

    status: str | None = Field(None, alias="status")

    type: str | None = Field(None, alias="type")
