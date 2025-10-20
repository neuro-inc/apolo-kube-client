from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ParamKind",)


class V1ParamKind(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None
