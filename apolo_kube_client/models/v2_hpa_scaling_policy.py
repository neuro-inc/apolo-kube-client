from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V2HPAScalingPolicy",)


class V2HPAScalingPolicy(BaseModel):
    period_seconds: int | None = Field(
        default=None,
        serialization_alias="periodSeconds",
        validation_alias=AliasChoices("period_seconds", "periodSeconds"),
    )

    type: str | None = None

    value: int | None = None
