from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector
from .v1_object_meta import V1ObjectMeta


class V1CSIStorageCapacity(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    capacity: str | None = Field(None, alias="capacity")

    kind: str | None = Field(None, alias="kind")

    maximum_volume_size: str | None = Field(None, alias="maximumVolumeSize")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    node_topology: V1LabelSelector | None = Field(None, alias="nodeTopology")

    storage_class_name: str | None = Field(None, alias="storageClassName")
