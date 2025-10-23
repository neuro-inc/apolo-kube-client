from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FCVolumeSource",)


class V1FCVolumeSource(BaseModel):
    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
        exclude_if=_exclude_if,
    )

    lun: int | None = Field(default=None, exclude_if=_exclude_if)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    target_ww_ns: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="targetWWNs",
            validation_alias=AliasChoices("target_ww_ns", "targetWWNs"),
            exclude_if=_exclude_if,
        )
    )

    wwids: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )
