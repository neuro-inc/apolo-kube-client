from __future__ import annotations
from pydantic import BaseModel, Field
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
    access_modes: list[str] = Field(default_factory=lambda: [], alias="accessModes")

    aws_elastic_block_store: V1AWSElasticBlockStoreVolumeSource = Field(
        default_factory=lambda: V1AWSElasticBlockStoreVolumeSource(),
        alias="awsElasticBlockStore",
    )

    azure_disk: V1AzureDiskVolumeSource = Field(
        default_factory=lambda: V1AzureDiskVolumeSource(), alias="azureDisk"
    )

    azure_file: V1AzureFilePersistentVolumeSource = Field(
        default_factory=lambda: V1AzureFilePersistentVolumeSource(), alias="azureFile"
    )

    capacity: dict[str, str] = Field(default_factory=lambda: {}, alias="capacity")

    cephfs: V1CephFSPersistentVolumeSource = Field(
        default_factory=lambda: V1CephFSPersistentVolumeSource(), alias="cephfs"
    )

    cinder: V1CinderPersistentVolumeSource = Field(
        default_factory=lambda: V1CinderPersistentVolumeSource(), alias="cinder"
    )

    claim_ref: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(), alias="claimRef"
    )

    csi: V1CSIPersistentVolumeSource = Field(
        default_factory=lambda: V1CSIPersistentVolumeSource(), alias="csi"
    )

    fc: V1FCVolumeSource = Field(default_factory=lambda: V1FCVolumeSource(), alias="fc")

    flex_volume: V1FlexPersistentVolumeSource = Field(
        default_factory=lambda: V1FlexPersistentVolumeSource(), alias="flexVolume"
    )

    flocker: V1FlockerVolumeSource = Field(
        default_factory=lambda: V1FlockerVolumeSource(), alias="flocker"
    )

    gce_persistent_disk: V1GCEPersistentDiskVolumeSource = Field(
        default_factory=lambda: V1GCEPersistentDiskVolumeSource(),
        alias="gcePersistentDisk",
    )

    glusterfs: V1GlusterfsPersistentVolumeSource = Field(
        default_factory=lambda: V1GlusterfsPersistentVolumeSource(), alias="glusterfs"
    )

    host_path: V1HostPathVolumeSource = Field(
        default_factory=lambda: V1HostPathVolumeSource(), alias="hostPath"
    )

    iscsi: V1ISCSIPersistentVolumeSource = Field(
        default_factory=lambda: V1ISCSIPersistentVolumeSource(), alias="iscsi"
    )

    local: V1LocalVolumeSource = Field(
        default_factory=lambda: V1LocalVolumeSource(), alias="local"
    )

    mount_options: list[str] = Field(default_factory=lambda: [], alias="mountOptions")

    nfs: V1NFSVolumeSource = Field(
        default_factory=lambda: V1NFSVolumeSource(), alias="nfs"
    )

    node_affinity: V1VolumeNodeAffinity = Field(
        default_factory=lambda: V1VolumeNodeAffinity(), alias="nodeAffinity"
    )

    persistent_volume_reclaim_policy: str | None = Field(
        default_factory=lambda: None, alias="persistentVolumeReclaimPolicy"
    )

    photon_persistent_disk: V1PhotonPersistentDiskVolumeSource = Field(
        default_factory=lambda: V1PhotonPersistentDiskVolumeSource(),
        alias="photonPersistentDisk",
    )

    portworx_volume: V1PortworxVolumeSource = Field(
        default_factory=lambda: V1PortworxVolumeSource(), alias="portworxVolume"
    )

    quobyte: V1QuobyteVolumeSource = Field(
        default_factory=lambda: V1QuobyteVolumeSource(), alias="quobyte"
    )

    rbd: V1RBDPersistentVolumeSource = Field(
        default_factory=lambda: V1RBDPersistentVolumeSource(), alias="rbd"
    )

    scale_io: V1ScaleIOPersistentVolumeSource = Field(
        default_factory=lambda: V1ScaleIOPersistentVolumeSource(), alias="scaleIO"
    )

    storage_class_name: str | None = Field(
        default_factory=lambda: None, alias="storageClassName"
    )

    storageos: V1StorageOSPersistentVolumeSource = Field(
        default_factory=lambda: V1StorageOSPersistentVolumeSource(), alias="storageos"
    )

    volume_attributes_class_name: str | None = Field(
        default_factory=lambda: None, alias="volumeAttributesClassName"
    )

    volume_mode: str | None = Field(default_factory=lambda: None, alias="volumeMode")

    vsphere_volume: V1VsphereVirtualDiskVolumeSource = Field(
        default_factory=lambda: V1VsphereVirtualDiskVolumeSource(),
        alias="vsphereVolume",
    )
