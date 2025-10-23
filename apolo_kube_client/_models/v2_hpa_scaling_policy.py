from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V2HPAScalingPolicy",)


class V2HPAScalingPolicy(BaseModel):
    period_seconds: int | None = Field(
        default=None,
        serialization_alias="periodSeconds",
        validation_alias=AliasChoices("period_seconds", "periodSeconds"),
        exclude_if=_exclude_if,
    )

    type: str | None = Field(default=None, exclude_if=_exclude_if)

    value: int | None = Field(default=None, exclude_if=_exclude_if)
