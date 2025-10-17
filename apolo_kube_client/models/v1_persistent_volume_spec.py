from pydantic import AliasChoices, BaseModel, Field
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

__all__ = ("V1PersistentVolumeSpec",)


class V1PersistentVolumeSpec(BaseModel):
    access_modes: list[str] = Field(
        default=[],
        serialization_alias="accessModes",
        validation_alias=AliasChoices("access_modes", "accessModes"),
    )

    aws_elastic_block_store: V1AWSElasticBlockStoreVolumeSource = Field(
        default_factory=lambda: V1AWSElasticBlockStoreVolumeSource(),
        serialization_alias="awsElasticBlockStore",
        validation_alias=AliasChoices(
            "aws_elastic_block_store", "awsElasticBlockStore"
        ),
    )

    azure_disk: V1AzureDiskVolumeSource = Field(
        default_factory=lambda: V1AzureDiskVolumeSource(),
        serialization_alias="azureDisk",
        validation_alias=AliasChoices("azure_disk", "azureDisk"),
    )

    azure_file: V1AzureFilePersistentVolumeSource = Field(
        default_factory=lambda: V1AzureFilePersistentVolumeSource(),
        serialization_alias="azureFile",
        validation_alias=AliasChoices("azure_file", "azureFile"),
    )

    capacity: dict[str, str] = {}

    cephfs: V1CephFSPersistentVolumeSource = Field(
        default_factory=lambda: V1CephFSPersistentVolumeSource()
    )

    cinder: V1CinderPersistentVolumeSource = Field(
        default_factory=lambda: V1CinderPersistentVolumeSource()
    )

    claim_ref: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="claimRef",
        validation_alias=AliasChoices("claim_ref", "claimRef"),
    )

    csi: V1CSIPersistentVolumeSource = Field(
        default_factory=lambda: V1CSIPersistentVolumeSource()
    )

    fc: V1FCVolumeSource = Field(default_factory=lambda: V1FCVolumeSource())

    flex_volume: V1FlexPersistentVolumeSource = Field(
        default_factory=lambda: V1FlexPersistentVolumeSource(),
        serialization_alias="flexVolume",
        validation_alias=AliasChoices("flex_volume", "flexVolume"),
    )

    flocker: V1FlockerVolumeSource = Field(
        default_factory=lambda: V1FlockerVolumeSource()
    )

    gce_persistent_disk: V1GCEPersistentDiskVolumeSource = Field(
        default_factory=lambda: V1GCEPersistentDiskVolumeSource(),
        serialization_alias="gcePersistentDisk",
        validation_alias=AliasChoices("gce_persistent_disk", "gcePersistentDisk"),
    )

    glusterfs: V1GlusterfsPersistentVolumeSource = Field(
        default_factory=lambda: V1GlusterfsPersistentVolumeSource()
    )

    host_path: V1HostPathVolumeSource = Field(
        default_factory=lambda: V1HostPathVolumeSource(),
        serialization_alias="hostPath",
        validation_alias=AliasChoices("host_path", "hostPath"),
    )

    iscsi: V1ISCSIPersistentVolumeSource = Field(
        default_factory=lambda: V1ISCSIPersistentVolumeSource()
    )

    local: V1LocalVolumeSource = Field(default_factory=lambda: V1LocalVolumeSource())

    mount_options: list[str] = Field(
        default=[],
        serialization_alias="mountOptions",
        validation_alias=AliasChoices("mount_options", "mountOptions"),
    )

    nfs: V1NFSVolumeSource = Field(default_factory=lambda: V1NFSVolumeSource())

    node_affinity: V1VolumeNodeAffinity = Field(
        default_factory=lambda: V1VolumeNodeAffinity(),
        serialization_alias="nodeAffinity",
        validation_alias=AliasChoices("node_affinity", "nodeAffinity"),
    )

    persistent_volume_reclaim_policy: str | None = Field(
        default=None,
        serialization_alias="persistentVolumeReclaimPolicy",
        validation_alias=AliasChoices(
            "persistent_volume_reclaim_policy", "persistentVolumeReclaimPolicy"
        ),
    )

    photon_persistent_disk: V1PhotonPersistentDiskVolumeSource = Field(
        default_factory=lambda: V1PhotonPersistentDiskVolumeSource(),
        serialization_alias="photonPersistentDisk",
        validation_alias=AliasChoices("photon_persistent_disk", "photonPersistentDisk"),
    )

    portworx_volume: V1PortworxVolumeSource = Field(
        default_factory=lambda: V1PortworxVolumeSource(),
        serialization_alias="portworxVolume",
        validation_alias=AliasChoices("portworx_volume", "portworxVolume"),
    )

    quobyte: V1QuobyteVolumeSource = Field(
        default_factory=lambda: V1QuobyteVolumeSource()
    )

    rbd: V1RBDPersistentVolumeSource = Field(
        default_factory=lambda: V1RBDPersistentVolumeSource()
    )

    scale_io: V1ScaleIOPersistentVolumeSource = Field(
        default_factory=lambda: V1ScaleIOPersistentVolumeSource(),
        serialization_alias="scaleIO",
        validation_alias=AliasChoices("scale_io", "scaleIO"),
    )

    storage_class_name: str | None = Field(
        default=None,
        serialization_alias="storageClassName",
        validation_alias=AliasChoices("storage_class_name", "storageClassName"),
    )

    storageos: V1StorageOSPersistentVolumeSource = Field(
        default_factory=lambda: V1StorageOSPersistentVolumeSource()
    )

    volume_attributes_class_name: str | None = Field(
        default=None,
        serialization_alias="volumeAttributesClassName",
        validation_alias=AliasChoices(
            "volume_attributes_class_name", "volumeAttributesClassName"
        ),
    )

    volume_mode: str | None = Field(
        default=None,
        serialization_alias="volumeMode",
        validation_alias=AliasChoices("volume_mode", "volumeMode"),
    )

    vsphere_volume: V1VsphereVirtualDiskVolumeSource = Field(
        default_factory=lambda: V1VsphereVirtualDiskVolumeSource(),
        serialization_alias="vsphereVolume",
        validation_alias=AliasChoices("vsphere_volume", "vsphereVolume"),
    )
