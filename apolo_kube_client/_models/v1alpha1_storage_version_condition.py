from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1alpha1StorageVersionCondition",)


class V1alpha1StorageVersionCondition(BaseModel):
    last_transition_time: datetime | None = Field(
        default=None,
        serialization_alias="lastTransitionTime",
        validation_alias=AliasChoices("last_transition_time", "lastTransitionTime"),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
        exclude_if=_exclude_if,
    )

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    status: str | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
