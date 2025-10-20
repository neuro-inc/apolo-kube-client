from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1beta1DeviceToleration",)


class V1beta1DeviceToleration(BaseModel):
    effect: str | None = None

    key: str | None = None

    operator: str | None = None

    toleration_seconds: int | None = Field(
        default=None,
        serialization_alias="tolerationSeconds",
        validation_alias=AliasChoices("toleration_seconds", "tolerationSeconds"),
    )

    value: str | None = None
