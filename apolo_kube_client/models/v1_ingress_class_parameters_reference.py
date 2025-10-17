from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1IngressClassParametersReference",)


class V1IngressClassParametersReference(BaseModel):
    api_group: str | None = Field(
        default=None,
        serialization_alias="apiGroup",
        validation_alias=AliasChoices("api_group", "apiGroup"),
    )

    kind: str | None = None

    name: str | None = None

    namespace: str | None = None

    scope: str | None = None
