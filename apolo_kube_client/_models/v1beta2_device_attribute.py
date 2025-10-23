from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1beta2DeviceAttribute",)


class V1beta2DeviceAttribute(BaseModel):
    bool_: bool | None = Field(
        default=None,
        serialization_alias="bool",
        validation_alias=AliasChoices("bool_", "bool"),
        exclude_if=_exclude_if,
    )

    int_: int | None = Field(
        default=None,
        serialization_alias="int",
        validation_alias=AliasChoices("int_", "int"),
        exclude_if=_exclude_if,
    )

    string: str | None = Field(default=None, exclude_if=_exclude_if)

    version: str | None = Field(default=None, exclude_if=_exclude_if)
