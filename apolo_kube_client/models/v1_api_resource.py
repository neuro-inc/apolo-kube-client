from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1APIResource",)


class V1APIResource(BaseModel):
    categories: list[str] = []

    group: str | None = None

    kind: str | None = None

    name: str | None = None

    namespaced: bool | None = None

    short_names: list[str] = Field(
        default=[],
        serialization_alias="shortNames",
        validation_alias=AliasChoices("short_names", "shortNames"),
    )

    singular_name: str | None = Field(
        default=None,
        serialization_alias="singularName",
        validation_alias=AliasChoices("singular_name", "singularName"),
    )

    storage_version_hash: str | None = Field(
        default=None,
        serialization_alias="storageVersionHash",
        validation_alias=AliasChoices("storage_version_hash", "storageVersionHash"),
    )

    verbs: list[str] = []

    version: str | None = None
