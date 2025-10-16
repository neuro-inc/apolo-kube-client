from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_topology_selector_term import V1TopologySelectorTerm

__all__ = ("V1StorageClass",)


class V1StorageClass(BaseModel):
    allow_volume_expansion: bool | None = Field(
        default_factory=lambda: None, alias="allowVolumeExpansion"
    )

    allowed_topologies: list[V1TopologySelectorTerm] = Field(
        default_factory=lambda: [], alias="allowedTopologies"
    )

    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    mount_options: list[str] = Field(default_factory=lambda: [], alias="mountOptions")

    parameters: dict[str, str] = Field(default_factory=lambda: {}, alias="parameters")

    provisioner: str | None = Field(default_factory=lambda: None, alias="provisioner")

    reclaim_policy: str | None = Field(
        default_factory=lambda: None, alias="reclaimPolicy"
    )

    volume_binding_mode: str | None = Field(
        default_factory=lambda: None, alias="volumeBindingMode"
    )
