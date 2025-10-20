from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V2MetricTarget",)


class V2MetricTarget(BaseModel):
    average_utilization: int | None = Field(
        default=None,
        serialization_alias="averageUtilization",
        validation_alias=AliasChoices("average_utilization", "averageUtilization"),
    )

    average_value: str | None = Field(
        default=None,
        serialization_alias="averageValue",
        validation_alias=AliasChoices("average_value", "averageValue"),
    )

    type: str | None = None

    value: str | None = None
