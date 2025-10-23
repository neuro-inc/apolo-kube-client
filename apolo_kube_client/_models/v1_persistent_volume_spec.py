from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_aws_elastic_block_store_volume_source import V1AWSElasticBlockStoreVolumeSource
from .v1_azure_disk_volume_source import V1AzureDiskVolumeSource
from .v1_azure_file_persistent_volume_source import V1AzureFilePersistentVolumeSource
from .v1_ceph_fs_persistent_volume_source import V1CephFSPersistentVolumeSource
from .v1_cinder_persistent_volume_source import V1CinderPersistentVolumeSource
from .v1_csi_persistent_volume_source import V1CSIPersistentVolumeSource
from .v1_fc_volume_source import V1FCVolumeSource
from .v1_flex_persistent_volume_source import V1FlexPersistentVolumeSource
from .v1_flocker_volume_source import V1FlockerVolumeSource
from .v1_gce_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource
from .v1_glusterfs_persistent_volume_source import V1GlusterfsPersistentVolumeSource
from .v1_host_path_volume_source import V1HostPathVolumeSource
from .v1_iscsi_persistent_volume_source import V1ISCSIPersistentVolumeSource
from .v1_local_volume_source import V1LocalVolumeSource
from .v1_nfs_volume_source import V1NFSVolumeSource
from .v1_object_reference import V1ObjectReference
from .v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource
from .v1_portworx_volume_source import V1PortworxVolumeSource
from .v1_quobyte_volume_source import V1QuobyteVolumeSource
from .v1_rbd_persistent_volume_source import V1RBDPersistentVolumeSource
from .v1_scale_io_persistent_volume_source import V1ScaleIOPersistentVolumeSource
from .v1_storage_os_persistent_volume_source import V1StorageOSPersistentVolumeSource
from .v1_volume_node_affinity import V1VolumeNodeAffinity
from .v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PersistentVolumeSpec",)


class V1PersistentVolumeSpec(BaseModel):
    access_modes: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="accessModes",
            validation_alias=AliasChoices("access_modes", "accessModes"),
            exclude_if=_exclude_if,
        )
    )

    aws_elastic_block_store: Annotated[
        V1AWSElasticBlockStoreVolumeSource,
        BeforeValidator(_default_if_none(V1AWSElasticBlockStoreVolumeSource)),
    ] = Field(
        default_factory=lambda: V1AWSElasticBlockStoreVolumeSource(),
        serialization_alias="awsElasticBlockStore",
        validation_alias=AliasChoices(
            "aws_elastic_block_store", "awsElasticBlockStore"
        ),
        exclude_if=_exclude_if,
    )

    azure_disk: Annotated[
        V1AzureDiskVolumeSource,
        BeforeValidator(_default_if_none(V1AzureDiskVolumeSource)),
    ] = Field(
        default_factory=lambda: V1AzureDiskVolumeSource(),
        serialization_alias="azureDisk",
        validation_alias=AliasChoices("azure_disk", "azureDisk"),
        exclude_if=_exclude_if,
    )

    azure_file: Annotated[
        V1AzureFilePersistentVolumeSource,
        BeforeValidator(_default_if_none(V1AzureFilePersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1AzureFilePersistentVolumeSource(),
        serialization_alias="azureFile",
        validation_alias=AliasChoices("azure_file", "azureFile"),
        exclude_if=_exclude_if,
    )

    capacity: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = (
        Field(default={}, exclude_if=_exclude_if)
    )

    cephfs: Annotated[
        V1CephFSPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1CephFSPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1CephFSPersistentVolumeSource(), exclude_if=_exclude_if
    )

    cinder: Annotated[
        V1CinderPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1CinderPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1CinderPersistentVolumeSource(), exclude_if=_exclude_if
    )

    claim_ref: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="claimRef",
        validation_alias=AliasChoices("claim_ref", "claimRef"),
        exclude_if=_exclude_if,
    )

    csi: Annotated[
        V1CSIPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1CSIPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1CSIPersistentVolumeSource(), exclude_if=_exclude_if
    )

    fc: Annotated[
        V1FCVolumeSource, BeforeValidator(_default_if_none(V1FCVolumeSource))
    ] = Field(default_factory=lambda: V1FCVolumeSource(), exclude_if=_exclude_if)

    flex_volume: Annotated[
        V1FlexPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1FlexPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1FlexPersistentVolumeSource(),
        serialization_alias="flexVolume",
        validation_alias=AliasChoices("flex_volume", "flexVolume"),
        exclude_if=_exclude_if,
    )

    flocker: Annotated[
        V1FlockerVolumeSource, BeforeValidator(_default_if_none(V1FlockerVolumeSource))
    ] = Field(default_factory=lambda: V1FlockerVolumeSource(), exclude_if=_exclude_if)

    gce_persistent_disk: Annotated[
        V1GCEPersistentDiskVolumeSource,
        BeforeValidator(_default_if_none(V1GCEPersistentDiskVolumeSource)),
    ] = Field(
        default_factory=lambda: V1GCEPersistentDiskVolumeSource(),
        serialization_alias="gcePersistentDisk",
        validation_alias=AliasChoices("gce_persistent_disk", "gcePersistentDisk"),
        exclude_if=_exclude_if,
    )

    glusterfs: Annotated[
        V1GlusterfsPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1GlusterfsPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1GlusterfsPersistentVolumeSource(),
        exclude_if=_exclude_if,
    )

    host_path: Annotated[
        V1HostPathVolumeSource,
        BeforeValidator(_default_if_none(V1HostPathVolumeSource)),
    ] = Field(
        default_factory=lambda: V1HostPathVolumeSource(),
        serialization_alias="hostPath",
        validation_alias=AliasChoices("host_path", "hostPath"),
        exclude_if=_exclude_if,
    )

    iscsi: Annotated[
        V1ISCSIPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1ISCSIPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1ISCSIPersistentVolumeSource(), exclude_if=_exclude_if
    )

    local: Annotated[
        V1LocalVolumeSource, BeforeValidator(_default_if_none(V1LocalVolumeSource))
    ] = Field(default_factory=lambda: V1LocalVolumeSource(), exclude_if=_exclude_if)

    mount_options: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="mountOptions",
            validation_alias=AliasChoices("mount_options", "mountOptions"),
            exclude_if=_exclude_if,
        )
    )

    nfs: Annotated[
        V1NFSVolumeSource, BeforeValidator(_default_if_none(V1NFSVolumeSource))
    ] = Field(default_factory=lambda: V1NFSVolumeSource(), exclude_if=_exclude_if)

    node_affinity: Annotated[
        V1VolumeNodeAffinity, BeforeValidator(_default_if_none(V1VolumeNodeAffinity))
    ] = Field(
        default_factory=lambda: V1VolumeNodeAffinity(),
        serialization_alias="nodeAffinity",
        validation_alias=AliasChoices("node_affinity", "nodeAffinity"),
        exclude_if=_exclude_if,
    )

    persistent_volume_reclaim_policy: str | None = Field(
        default=None,
        serialization_alias="persistentVolumeReclaimPolicy",
        validation_alias=AliasChoices(
            "persistent_volume_reclaim_policy", "persistentVolumeReclaimPolicy"
        ),
        exclude_if=_exclude_if,
    )

    photon_persistent_disk: Annotated[
        V1PhotonPersistentDiskVolumeSource,
        BeforeValidator(_default_if_none(V1PhotonPersistentDiskVolumeSource)),
    ] = Field(
        default_factory=lambda: V1PhotonPersistentDiskVolumeSource(),
        serialization_alias="photonPersistentDisk",
        validation_alias=AliasChoices("photon_persistent_disk", "photonPersistentDisk"),
        exclude_if=_exclude_if,
    )

    portworx_volume: Annotated[
        V1PortworxVolumeSource,
        BeforeValidator(_default_if_none(V1PortworxVolumeSource)),
    ] = Field(
        default_factory=lambda: V1PortworxVolumeSource(),
        serialization_alias="portworxVolume",
        validation_alias=AliasChoices("portworx_volume", "portworxVolume"),
        exclude_if=_exclude_if,
    )

    quobyte: Annotated[
        V1QuobyteVolumeSource, BeforeValidator(_default_if_none(V1QuobyteVolumeSource))
    ] = Field(default_factory=lambda: V1QuobyteVolumeSource(), exclude_if=_exclude_if)

    rbd: Annotated[
        V1RBDPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1RBDPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1RBDPersistentVolumeSource(), exclude_if=_exclude_if
    )

    scale_io: Annotated[
        V1ScaleIOPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1ScaleIOPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1ScaleIOPersistentVolumeSource(),
        serialization_alias="scaleIO",
        validation_alias=AliasChoices("scale_io", "scaleIO"),
        exclude_if=_exclude_if,
    )

    storage_class_name: str | None = Field(
        default=None,
        serialization_alias="storageClassName",
        validation_alias=AliasChoices("storage_class_name", "storageClassName"),
        exclude_if=_exclude_if,
    )

    storageos: Annotated[
        V1StorageOSPersistentVolumeSource,
        BeforeValidator(_default_if_none(V1StorageOSPersistentVolumeSource)),
    ] = Field(
        default_factory=lambda: V1StorageOSPersistentVolumeSource(),
        exclude_if=_exclude_if,
    )

    volume_attributes_class_name: str | None = Field(
        default=None,
        serialization_alias="volumeAttributesClassName",
        validation_alias=AliasChoices(
            "volume_attributes_class_name", "volumeAttributesClassName"
        ),
        exclude_if=_exclude_if,
    )

    volume_mode: str | None = Field(
        default=None,
        serialization_alias="volumeMode",
        validation_alias=AliasChoices("volume_mode", "volumeMode"),
        exclude_if=_exclude_if,
    )

    vsphere_volume: Annotated[
        V1VsphereVirtualDiskVolumeSource,
        BeforeValidator(_default_if_none(V1VsphereVirtualDiskVolumeSource)),
    ] = Field(
        default_factory=lambda: V1VsphereVirtualDiskVolumeSource(),
        serialization_alias="vsphereVolume",
        validation_alias=AliasChoices("vsphere_volume", "vsphereVolume"),
        exclude_if=_exclude_if,
    )
