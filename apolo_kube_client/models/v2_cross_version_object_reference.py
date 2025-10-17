from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V2CrossVersionObjectReference",)


class V2CrossVersionObjectReference(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    name: str | None = None
