from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1beta1DeviceToleration",)


class V1beta1DeviceToleration(BaseModel):
    effect: str | None = Field(default=None, exclude_if=_exclude_if)

    key: str | None = Field(default=None, exclude_if=_exclude_if)

    operator: str | None = Field(default=None, exclude_if=_exclude_if)

    toleration_seconds: int | None = Field(
        default=None,
        serialization_alias="tolerationSeconds",
        validation_alias=AliasChoices("toleration_seconds", "tolerationSeconds"),
        exclude_if=_exclude_if,
    )

    value: str | None = Field(default=None, exclude_if=_exclude_if)
