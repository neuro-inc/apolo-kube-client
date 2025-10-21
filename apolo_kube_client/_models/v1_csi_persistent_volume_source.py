from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CSIPersistentVolumeSource",)


class V1CSIPersistentVolumeSource(BaseModel):
    controller_expand_secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="controllerExpandSecretRef",
        validation_alias=AliasChoices(
            "controller_expand_secret_ref", "controllerExpandSecretRef"
        ),
    )

    controller_publish_secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="controllerPublishSecretRef",
        validation_alias=AliasChoices(
            "controller_publish_secret_ref", "controllerPublishSecretRef"
        ),
    )

    driver: str | None = None

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    node_expand_secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="nodeExpandSecretRef",
        validation_alias=AliasChoices("node_expand_secret_ref", "nodeExpandSecretRef"),
    )

    node_publish_secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="nodePublishSecretRef",
        validation_alias=AliasChoices(
            "node_publish_secret_ref", "nodePublishSecretRef"
        ),
    )

    node_stage_secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="nodeStageSecretRef",
        validation_alias=AliasChoices("node_stage_secret_ref", "nodeStageSecretRef"),
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

    volume_handle: str | None = Field(
        default=None,
        serialization_alias="volumeHandle",
        validation_alias=AliasChoices("volume_handle", "volumeHandle"),
    )
