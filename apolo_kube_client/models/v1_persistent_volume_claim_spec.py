from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector
from .v1_typed_local_object_reference import V1TypedLocalObjectReference
from .v1_typed_object_reference import V1TypedObjectReference
from .v1_volume_resource_requirements import V1VolumeResourceRequirements

__all__ = ("V1PersistentVolumeClaimSpec",)


class V1PersistentVolumeClaimSpec(BaseModel):
    access_modes: list[str] | None = Field(None, alias="accessModes")

    data_source: V1TypedLocalObjectReference | None = Field(None, alias="dataSource")

    data_source_ref: V1TypedObjectReference | None = Field(None, alias="dataSourceRef")

    resources: V1VolumeResourceRequirements | None = Field(None, alias="resources")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    storage_class_name: str | None = Field(None, alias="storageClassName")

    volume_attributes_class_name: str | None = Field(
        None, alias="volumeAttributesClassName"
    )

    volume_mode: str | None = Field(None, alias="volumeMode")

    volume_name: str | None = Field(None, alias="volumeName")
