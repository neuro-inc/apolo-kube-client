from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1beta2DeviceAttribute",)


class V1beta2DeviceAttribute(BaseModel):
    bool_: bool | None = Field(
        default=None,
        serialization_alias="bool",
        validation_alias=AliasChoices("bool_", "bool"),
    )

    int_: int | None = Field(
        default=None,
        serialization_alias="int",
        validation_alias=AliasChoices("int_", "int"),
    )

    string: str | None = None

    version: str | None = None
