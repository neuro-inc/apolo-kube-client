from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1PodCondition",)


class V1PodCondition(BaseModel):
    last_probe_time: datetime | None = Field(
        default=None,
        serialization_alias="lastProbeTime",
        validation_alias=AliasChoices("last_probe_time", "lastProbeTime"),
    )

    last_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastTransitionTime",
        validation_alias=AliasChoices("last_transition_time", "lastTransitionTime"),
    )

    message: str | None = None

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )

    reason: str | None = None

    status: str | None = None

    type: str | None = None
