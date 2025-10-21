from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_typed_local_object_reference import V1TypedLocalObjectReference
from .v1_typed_object_reference import V1TypedObjectReference
from .v1_volume_resource_requirements import V1VolumeResourceRequirements
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PersistentVolumeClaimSpec",)


class V1PersistentVolumeClaimSpec(BaseModel):
    access_modes: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="accessModes",
            validation_alias=AliasChoices("access_modes", "accessModes"),
        )
    )

    data_source: Annotated[
        V1TypedLocalObjectReference,
        BeforeValidator(_default_if_none(V1TypedLocalObjectReference)),
    ] = Field(
        default_factory=lambda: V1TypedLocalObjectReference(),
        serialization_alias="dataSource",
        validation_alias=AliasChoices("data_source", "dataSource"),
    )

    data_source_ref: Annotated[
        V1TypedObjectReference,
        BeforeValidator(_default_if_none(V1TypedObjectReference)),
    ] = Field(
        default_factory=lambda: V1TypedObjectReference(),
        serialization_alias="dataSourceRef",
        validation_alias=AliasChoices("data_source_ref", "dataSourceRef"),
    )

    resources: Annotated[
        V1VolumeResourceRequirements,
        BeforeValidator(_default_if_none(V1VolumeResourceRequirements)),
    ] = Field(default_factory=lambda: V1VolumeResourceRequirements())

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector())

    storage_class_name: str | None = Field(
        default=None,
        serialization_alias="storageClassName",
        validation_alias=AliasChoices("storage_class_name", "storageClassName"),
    )

    volume_attributes_class_name: str | None = Field(
        default=None,
        serialization_alias="volumeAttributesClassName",
        validation_alias=AliasChoices(
            "volume_attributes_class_name", "volumeAttributesClassName"
        ),
    )

    volume_mode: str | None = Field(
        default=None,
        serialization_alias="volumeMode",
        validation_alias=AliasChoices("volume_mode", "volumeMode"),
    )

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
    )
