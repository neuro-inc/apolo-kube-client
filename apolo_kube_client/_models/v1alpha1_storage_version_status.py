from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1alpha1_server_storage_version import V1alpha1ServerStorageVersion
from .v1alpha1_storage_version_condition import V1alpha1StorageVersionCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1StorageVersionStatus",)


class V1alpha1StorageVersionStatus(BaseModel):
    common_encoding_version: str | None = Field(
        default=None,
        serialization_alias="commonEncodingVersion",
        validation_alias=AliasChoices(
            "common_encoding_version", "commonEncodingVersion"
        ),
        exclude_if=_exclude_if,
    )

    conditions: Annotated[
        list[V1alpha1StorageVersionCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)

    storage_versions: Annotated[
        list[V1alpha1ServerStorageVersion], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="storageVersions",
        validation_alias=AliasChoices("storage_versions", "storageVersions"),
        exclude_if=_exclude_if,
    )
