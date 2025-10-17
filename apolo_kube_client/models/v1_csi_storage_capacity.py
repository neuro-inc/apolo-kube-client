from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CSIStorageCapacity",)


class V1CSIStorageCapacity(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    capacity: str | None = Field(default_factory=lambda: None)

    kind: str | None = Field(default_factory=lambda: None)

    maximum_volume_size: str | None = Field(
        default_factory=lambda: None, alias="maximumVolumeSize"
    )

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    node_topology: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="nodeTopology"
    )

    storage_class_name: str | None = Field(
        default_factory=lambda: None, alias="storageClassName"
    )
