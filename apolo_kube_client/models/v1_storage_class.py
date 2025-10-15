from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_topology_selector_term import V1TopologySelectorTerm


class V1StorageClass(BaseModel):
    allow_volume_expansion: bool | None = Field(None, alias="allowVolumeExpansion")

    allowed_topologies: list[V1TopologySelectorTerm] | None = Field(
        None, alias="allowedTopologies"
    )

    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    mount_options: list[str] | None = Field(None, alias="mountOptions")

    parameters: dict(str, str) | None = Field(None, alias="parameters")

    provisioner: str | None = Field(None, alias="provisioner")

    reclaim_policy: str | None = Field(None, alias="reclaimPolicy")

    volume_binding_mode: str | None = Field(None, alias="volumeBindingMode")
