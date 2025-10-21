from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_local_object_reference import V1LocalObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CSIVolumeSource",)


class V1CSIVolumeSource(BaseModel):
    driver: str | None = None

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    node_publish_secret_ref: Annotated[
        V1LocalObjectReference,
        BeforeValidator(_default_if_none(V1LocalObjectReference)),
    ] = Field(
        default_factory=lambda: V1LocalObjectReference(),
        serialization_alias="nodePublishSecretRef",
        validation_alias=AliasChoices(
            "node_publish_secret_ref", "nodePublishSecretRef"
        ),
    )

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    volume_attributes: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="volumeAttributes",
        validation_alias=AliasChoices("volume_attributes", "volumeAttributes"),
    )
