from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_aws_elastic_block_store_volume_source import V1AWSElasticBlockStoreVolumeSource
from .v1_azure_disk_volume_source import V1AzureDiskVolumeSource
from .v1_azure_file_volume_source import V1AzureFileVolumeSource
from .v1_ceph_fs_volume_source import V1CephFSVolumeSource
from .v1_cinder_volume_source import V1CinderVolumeSource
from .v1_config_map_volume_source import V1ConfigMapVolumeSource
from .v1_csi_volume_source import V1CSIVolumeSource
from .v1_downward_api_volume_source import V1DownwardAPIVolumeSource
from .v1_empty_dir_volume_source import V1EmptyDirVolumeSource
from .v1_ephemeral_volume_source import V1EphemeralVolumeSource
from .v1_fc_volume_source import V1FCVolumeSource
from .v1_flex_volume_source import V1FlexVolumeSource
from .v1_flocker_volume_source import V1FlockerVolumeSource
from .v1_gce_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource
from .v1_git_repo_volume_source import V1GitRepoVolumeSource
from .v1_glusterfs_volume_source import V1GlusterfsVolumeSource
from .v1_host_path_volume_source import V1HostPathVolumeSource
from .v1_image_volume_source import V1ImageVolumeSource
from .v1_iscsi_volume_source import V1ISCSIVolumeSource
from .v1_nfs_volume_source import V1NFSVolumeSource
from .v1_persistent_volume_claim_volume_source import (
    V1PersistentVolumeClaimVolumeSource,
)
from .v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource
from .v1_portworx_volume_source import V1PortworxVolumeSource
from .v1_projected_volume_source import V1ProjectedVolumeSource
from .v1_quobyte_volume_source import V1QuobyteVolumeSource
from .v1_rbd_volume_source import V1RBDVolumeSource
from .v1_scale_io_volume_source import V1ScaleIOVolumeSource
from .v1_secret_volume_source import V1SecretVolumeSource
from .v1_storage_os_volume_source import V1StorageOSVolumeSource
from .v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource

__all__ = ("V1Volume",)


class V1Volume(BaseModel):
    aws_elastic_block_store: V1AWSElasticBlockStoreVolumeSource = Field(
        default_factory=lambda: V1AWSElasticBlockStoreVolumeSource(),
        alias="awsElasticBlockStore",
    )

    azure_disk: V1AzureDiskVolumeSource = Field(
        default_factory=lambda: V1AzureDiskVolumeSource(), alias="azureDisk"
    )

    azure_file: V1AzureFileVolumeSource = Field(
        default_factory=lambda: V1AzureFileVolumeSource(), alias="azureFile"
    )

    cephfs: V1CephFSVolumeSource = Field(
        default_factory=lambda: V1CephFSVolumeSource(), alias="cephfs"
    )

    cinder: V1CinderVolumeSource = Field(
        default_factory=lambda: V1CinderVolumeSource(), alias="cinder"
    )

    config_map: V1ConfigMapVolumeSource = Field(
        default_factory=lambda: V1ConfigMapVolumeSource(), alias="configMap"
    )

    csi: V1CSIVolumeSource = Field(
        default_factory=lambda: V1CSIVolumeSource(), alias="csi"
    )

    downward_api: V1DownwardAPIVolumeSource = Field(
        default_factory=lambda: V1DownwardAPIVolumeSource(), alias="downwardAPI"
    )

    empty_dir: V1EmptyDirVolumeSource = Field(
        default_factory=lambda: V1EmptyDirVolumeSource(), alias="emptyDir"
    )

    ephemeral: V1EphemeralVolumeSource = Field(
        default_factory=lambda: V1EphemeralVolumeSource(), alias="ephemeral"
    )

    fc: V1FCVolumeSource = Field(default_factory=lambda: V1FCVolumeSource(), alias="fc")

    flex_volume: V1FlexVolumeSource = Field(
        default_factory=lambda: V1FlexVolumeSource(), alias="flexVolume"
    )

    flocker: V1FlockerVolumeSource = Field(
        default_factory=lambda: V1FlockerVolumeSource(), alias="flocker"
    )

    gce_persistent_disk: V1GCEPersistentDiskVolumeSource = Field(
        default_factory=lambda: V1GCEPersistentDiskVolumeSource(),
        alias="gcePersistentDisk",
    )

    git_repo: V1GitRepoVolumeSource = Field(
        default_factory=lambda: V1GitRepoVolumeSource(), alias="gitRepo"
    )

    glusterfs: V1GlusterfsVolumeSource = Field(
        default_factory=lambda: V1GlusterfsVolumeSource(), alias="glusterfs"
    )

    host_path: V1HostPathVolumeSource = Field(
        default_factory=lambda: V1HostPathVolumeSource(), alias="hostPath"
    )

    image: V1ImageVolumeSource = Field(
        default_factory=lambda: V1ImageVolumeSource(), alias="image"
    )

    iscsi: V1ISCSIVolumeSource = Field(
        default_factory=lambda: V1ISCSIVolumeSource(), alias="iscsi"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")

    nfs: V1NFSVolumeSource = Field(
        default_factory=lambda: V1NFSVolumeSource(), alias="nfs"
    )

    persistent_volume_claim: V1PersistentVolumeClaimVolumeSource = Field(
        default_factory=lambda: V1PersistentVolumeClaimVolumeSource(),
        alias="persistentVolumeClaim",
    )

    photon_persistent_disk: V1PhotonPersistentDiskVolumeSource = Field(
        default_factory=lambda: V1PhotonPersistentDiskVolumeSource(),
        alias="photonPersistentDisk",
    )

    portworx_volume: V1PortworxVolumeSource = Field(
        default_factory=lambda: V1PortworxVolumeSource(), alias="portworxVolume"
    )

    projected: V1ProjectedVolumeSource = Field(
        default_factory=lambda: V1ProjectedVolumeSource(), alias="projected"
    )

    quobyte: V1QuobyteVolumeSource = Field(
        default_factory=lambda: V1QuobyteVolumeSource(), alias="quobyte"
    )

    rbd: V1RBDVolumeSource = Field(
        default_factory=lambda: V1RBDVolumeSource(), alias="rbd"
    )

    scale_io: V1ScaleIOVolumeSource = Field(
        default_factory=lambda: V1ScaleIOVolumeSource(), alias="scaleIO"
    )

    secret: V1SecretVolumeSource = Field(
        default_factory=lambda: V1SecretVolumeSource(), alias="secret"
    )

    storageos: V1StorageOSVolumeSource = Field(
        default_factory=lambda: V1StorageOSVolumeSource(), alias="storageos"
    )

    vsphere_volume: V1VsphereVirtualDiskVolumeSource = Field(
        default_factory=lambda: V1VsphereVirtualDiskVolumeSource(),
        alias="vsphereVolume",
    )
