from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1ServerStorageVersion",)


class V1alpha1ServerStorageVersion(BaseModel):
    api_server_id: str | None = Field(
        default=None,
        serialization_alias="apiServerID",
        validation_alias=AliasChoices("api_server_id", "apiServerID"),
        exclude_if=_exclude_if,
    )

    decodable_versions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="decodableVersions",
        validation_alias=AliasChoices("decodable_versions", "decodableVersions"),
        exclude_if=_exclude_if,
    )

    encoding_version: str | None = Field(
        default=None,
        serialization_alias="encodingVersion",
        validation_alias=AliasChoices("encoding_version", "encodingVersion"),
        exclude_if=_exclude_if,
    )

    served_versions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="servedVersions",
        validation_alias=AliasChoices("served_versions", "servedVersions"),
        exclude_if=_exclude_if,
    )
