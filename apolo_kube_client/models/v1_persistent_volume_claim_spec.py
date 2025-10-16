from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_typed_local_object_reference import V1TypedLocalObjectReference
from .v1_typed_object_reference import V1TypedObjectReference
from .v1_volume_resource_requirements import V1VolumeResourceRequirements

__all__ = ("V1PersistentVolumeClaimSpec",)


class V1PersistentVolumeClaimSpec(BaseModel):
    access_modes: list[str] = Field(default_factory=lambda: [], alias="accessModes")

    data_source: V1TypedLocalObjectReference = Field(
        default_factory=lambda: V1TypedLocalObjectReference(), alias="dataSource"
    )

    data_source_ref: V1TypedObjectReference = Field(
        default_factory=lambda: V1TypedObjectReference(), alias="dataSourceRef"
    )

    resources: V1VolumeResourceRequirements = Field(
        default_factory=lambda: V1VolumeResourceRequirements(), alias="resources"
    )

    selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="selector"
    )

    storage_class_name: str | None = Field(
        default_factory=lambda: None, alias="storageClassName"
    )

    volume_attributes_class_name: str | None = Field(
        default_factory=lambda: None, alias="volumeAttributesClassName"
    )

    volume_mode: str | None = Field(default_factory=lambda: None, alias="volumeMode")

    volume_name: str | None = Field(default_factory=lambda: None, alias="volumeName")
