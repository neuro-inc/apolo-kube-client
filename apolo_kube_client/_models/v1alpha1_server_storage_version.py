from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1alpha1ServerStorageVersion",)


class V1alpha1ServerStorageVersion(BaseModel):
    api_server_id: str | None = Field(
        default=None,
        serialization_alias="apiServerID",
        validation_alias=AliasChoices("api_server_id", "apiServerID"),
    )

    decodable_versions: list[str] = Field(
        default=[],
        serialization_alias="decodableVersions",
        validation_alias=AliasChoices("decodable_versions", "decodableVersions"),
    )

    encoding_version: str | None = Field(
        default=None,
        serialization_alias="encodingVersion",
        validation_alias=AliasChoices("encoding_version", "encodingVersion"),
    )

    served_versions: list[str] = Field(
        default=[],
        serialization_alias="servedVersions",
        validation_alias=AliasChoices("served_versions", "servedVersions"),
    )
