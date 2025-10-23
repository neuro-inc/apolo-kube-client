from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1SelectableField",)


class V1SelectableField(BaseModel):
    json_path: str | None = Field(
        default=None,
        serialization_alias="jsonPath",
        validation_alias=AliasChoices("json_path", "jsonPath"),
        exclude_if=_exclude_if,
    )
