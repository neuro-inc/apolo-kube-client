from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DownwardAPIVolumeSource",)


class V1DownwardAPIVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
        exclude_if=_exclude_if,
    )

    items: Annotated[
        list[V1DownwardAPIVolumeFile], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
