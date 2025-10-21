from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_topology_selector_term import V1TopologySelectorTerm
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1StorageClass",)


class V1StorageClass(ResourceModel):
    allow_volume_expansion: bool | None = Field(
        default=None,
        serialization_alias="allowVolumeExpansion",
        validation_alias=AliasChoices("allow_volume_expansion", "allowVolumeExpansion"),
    )

    allowed_topologies: Annotated[
        list[V1TopologySelectorTerm], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="allowedTopologies",
        validation_alias=AliasChoices("allowed_topologies", "allowedTopologies"),
    )

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    mount_options: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="mountOptions",
            validation_alias=AliasChoices("mount_options", "mountOptions"),
        )
    )

    parameters: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    provisioner: str | None = None

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
