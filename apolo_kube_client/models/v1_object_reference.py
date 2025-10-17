from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ObjectReference",)


class V1ObjectReference(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    field_path: str | None = Field(
        default=None,
        serialization_alias="fieldPath",
        validation_alias=AliasChoices("field_path", "fieldPath"),
    )

    kind: str | None = None

    name: str | None = None

    namespace: str | None = None

    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
    )

    uid: str | None = None
