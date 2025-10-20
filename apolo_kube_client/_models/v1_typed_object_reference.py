from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1TypedObjectReference",)


class V1TypedObjectReference(BaseModel):
    api_group: str | None = Field(
        default=None,
        serialization_alias="apiGroup",
        validation_alias=AliasChoices("api_group", "apiGroup"),
    )

    kind: str | None = None

    name: str | None = None

    namespace: str | None = None
