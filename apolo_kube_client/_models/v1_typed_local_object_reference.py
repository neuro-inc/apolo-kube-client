from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1TypedLocalObjectReference",)


class V1TypedLocalObjectReference(BaseModel):
    api_group: str | None = Field(
        default=None,
        serialization_alias="apiGroup",
        validation_alias=AliasChoices("api_group", "apiGroup"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)
