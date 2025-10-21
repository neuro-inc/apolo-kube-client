from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_local_object_reference import V1LocalObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FlexVolumeSource",)


class V1FlexVolumeSource(BaseModel):
    driver: str | None = None

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    options: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_ref: Annotated[
        V1LocalObjectReference,
        BeforeValidator(_default_if_none(V1LocalObjectReference)),
    ] = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )
