from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1Preconditions",)


class V1Preconditions(BaseModel):
    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
    )

    uid: str | None = None
