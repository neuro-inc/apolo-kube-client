from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1CustomResourceColumnDefinition",)


class V1CustomResourceColumnDefinition(BaseModel):
    description: str | None = Field(default=None, exclude_if=_exclude_if)

    format: str | None = Field(default=None, exclude_if=_exclude_if)

    json_path: str | None = Field(
        default=None,
        serialization_alias="jsonPath",
        validation_alias=AliasChoices("json_path", "jsonPath"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    priority: int | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
