from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_topology_selector_term import V1TopologySelectorTerm
from pydantic import BeforeValidator

__all__ = ("V1StorageClass",)


class V1StorageClass(ResourceModel):
    """StorageClass describes the parameters for a class of storage for which PersistentVolumes can be dynamically provisioned.

    StorageClasses are non-namespaced; the name of the storage class according to etcd is in ObjectMeta.Name."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.StorageClass"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="storage.k8s.io", kind="StorageClass", version="v1"
    )

    allow_volume_expansion: Annotated[
        bool | None,
        Field(
            alias="allowVolumeExpansion",
            description="""allowVolumeExpansion shows whether the storage class allow volume expand.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    allowed_topologies: Annotated[
        list[V1TopologySelectorTerm],
        Field(
            alias="allowedTopologies",
            description="""allowedTopologies restrict the node topologies where volumes can be dynamically provisioned. Each volume plugin defines its own supported topology specifications. An empty TopologySelectorTerm list means there is no topology restriction. This field is only honored by servers that enable the VolumeScheduling feature.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "storage.k8s.io/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "StorageClass"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    mount_options: Annotated[
        list[str],
        Field(
            alias="mountOptions",
            description="""mountOptions controls the mountOptions for dynamically provisioned PersistentVolumes of this storage class. e.g. ["ro", "soft"]. Not validated - mount of the PVs will simply fail if one is invalid.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    parameters: Annotated[
        dict[str, str],
        Field(
            description="""parameters holds the parameters for the provisioner that should create volumes of this storage class.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    provisioner: Annotated[
        str, Field(description="""provisioner indicates the type of the provisioner.""")
    ]

    reclaim_policy: Annotated[
        str | None,
        Field(
            alias="reclaimPolicy",
            description="""reclaimPolicy controls the reclaimPolicy for dynamically provisioned PersistentVolumes of this storage class. Defaults to Delete.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_binding_mode: Annotated[
        str | None,
        Field(
            alias="volumeBindingMode",
            description="""volumeBindingMode indicates how PersistentVolumeClaims should be provisioned and bound.  When unset, VolumeBindingImmediate is used. This field is only honored by servers that enable the VolumeScheduling feature.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
