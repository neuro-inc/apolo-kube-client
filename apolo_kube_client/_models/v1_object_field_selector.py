from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ObjectFieldSelector",)


class V1ObjectFieldSelector(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    field_path: str | None = Field(
        default=None,
        serialization_alias="fieldPath",
        validation_alias=AliasChoices("field_path", "fieldPath"),
        exclude_if=_exclude_if,
    )
