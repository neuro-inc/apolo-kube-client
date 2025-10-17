from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1CustomResourceColumnDefinition",)


class V1CustomResourceColumnDefinition(BaseModel):
    description: str | None = None

    format: str | None = None

    json_path: str | None = Field(
        default=None,
        serialization_alias="jsonPath",
        validation_alias=AliasChoices("json_path", "jsonPath"),
    )

    name: str | None = None

    priority: int | None = None

    type: str | None = None
