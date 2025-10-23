from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V2MetricTarget",)


class V2MetricTarget(BaseModel):
    average_utilization: int | None = Field(
        default=None,
        serialization_alias="averageUtilization",
        validation_alias=AliasChoices("average_utilization", "averageUtilization"),
        exclude_if=_exclude_if,
    )

    average_value: str | None = Field(
        default=None,
        serialization_alias="averageValue",
        validation_alias=AliasChoices("average_value", "averageValue"),
        exclude_if=_exclude_if,
    )

    type: str | None = Field(default=None, exclude_if=_exclude_if)

    value: str | None = Field(default=None, exclude_if=_exclude_if)
