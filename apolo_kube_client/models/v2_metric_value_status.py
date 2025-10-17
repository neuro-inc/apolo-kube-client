from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V2MetricValueStatus",)


class V2MetricValueStatus(BaseModel):
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

    value: str | None = None
