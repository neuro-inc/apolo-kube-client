from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_volume_projection import V1VolumeProjection
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ProjectedVolumeSource",)


class V1ProjectedVolumeSource(BaseModel):
    default_mode: int | None = Field(
        default=None,
        serialization_alias="defaultMode",
        validation_alias=AliasChoices("default_mode", "defaultMode"),
    )

    sources: Annotated[
        list[V1VolumeProjection], BeforeValidator(_collection_if_none("[]"))
    ] = []
