from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_key_to_path import V1KeyToPath
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SecretVolumeSource",)


class V1SecretVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    items: Annotated[list[V1KeyToPath], BeforeValidator(_collection_if_none("[]"))] = []

    optional: bool | None = None

    secret_name: str | None = Field(
        default=None,
        serialization_alias="secretName",
        validation_alias=AliasChoices("secret_name", "secretName"),
    )
