from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1SelectableField",)


class V1SelectableField(BaseModel):
    json_path: str | None = Field(
        default=None,
        serialization_alias="jsonPath",
        validation_alias=AliasChoices("json_path", "jsonPath"),
    )
