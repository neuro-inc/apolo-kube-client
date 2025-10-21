from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FCVolumeSource",)


class V1FCVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    lun: int | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    target_ww_ns: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="targetWWNs",
            validation_alias=AliasChoices("target_ww_ns", "targetWWNs"),
        )
    )

    wwids: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
