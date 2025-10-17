from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_topology_selector_term import V1TopologySelectorTerm

__all__ = ("V1StorageClass",)


class V1StorageClass(BaseModel):
    allow_volume_expansion: bool | None = Field(
        default=None,
        serialization_alias="allowVolumeExpansion",
        validation_alias=AliasChoices("allow_volume_expansion", "allowVolumeExpansion"),
    )

    allowed_topologies: list[V1TopologySelectorTerm] = Field(
        default=[],
        serialization_alias="allowedTopologies",
        validation_alias=AliasChoices("allowed_topologies", "allowedTopologies"),
    )

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    mount_options: list[str] = Field(
        default=[],
        serialization_alias="mountOptions",
        validation_alias=AliasChoices("mount_options", "mountOptions"),
    )

    parameters: dict[str, str] = Field(default={})

    provisioner: str | None = Field(default=None)

    reclaim_policy: str | None = Field(
        default=None,
        serialization_alias="reclaimPolicy",
        validation_alias=AliasChoices("reclaim_policy", "reclaimPolicy"),
    )

    volume_binding_mode: str | None = Field(
        default=None,
        serialization_alias="volumeBindingMode",
        validation_alias=AliasChoices("volume_binding_mode", "volumeBindingMode"),
    )
