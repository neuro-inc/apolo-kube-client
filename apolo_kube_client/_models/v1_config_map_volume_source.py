from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_key_to_path import V1KeyToPath
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ConfigMapVolumeSource",)


class V1ConfigMapVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    items: Annotated[list[V1KeyToPath], BeforeValidator(_collection_if_none("[]"))] = []

    name: str | None = None

    optional: bool | None = None
