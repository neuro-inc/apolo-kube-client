from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
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

    azure_file: V1AzureFileVolumeSource = Field(
        default_factory=lambda: V1AzureFileVolumeSource(),
        serialization_alias="azureFile",
        validation_alias=AliasChoices("azure_file", "azureFile"),
    )

    cephfs: V1CephFSVolumeSource = Field(default_factory=lambda: V1CephFSVolumeSource())

    cinder: V1CinderVolumeSource = Field(default_factory=lambda: V1CinderVolumeSource())

    config_map: V1ConfigMapVolumeSource = Field(
        default_factory=lambda: V1ConfigMapVolumeSource(),
        serialization_alias="configMap",
        validation_alias=AliasChoices("config_map", "configMap"),
    )

    csi: V1CSIVolumeSource = Field(default_factory=lambda: V1CSIVolumeSource())

    downward_api: V1DownwardAPIVolumeSource = Field(
        default_factory=lambda: V1DownwardAPIVolumeSource(),
        serialization_alias="downwardAPI",
        validation_alias=AliasChoices("downward_api", "downwardAPI"),
    )

    empty_dir: V1EmptyDirVolumeSource = Field(
        default_factory=lambda: V1EmptyDirVolumeSource(),
        serialization_alias="emptyDir",
        validation_alias=AliasChoices("empty_dir", "emptyDir"),
    )

    ephemeral: V1EphemeralVolumeSource = Field(
        default_factory=lambda: V1EphemeralVolumeSource()
    )

    fc: V1FCVolumeSource = Field(default_factory=lambda: V1FCVolumeSource())

    flex_volume: V1FlexVolumeSource = Field(
        default_factory=lambda: V1FlexVolumeSource(),
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

    git_repo: V1GitRepoVolumeSource = Field(
        default_factory=lambda: V1GitRepoVolumeSource(),
        serialization_alias="gitRepo",
        validation_alias=AliasChoices("git_repo", "gitRepo"),
    )

    glusterfs: V1GlusterfsVolumeSource = Field(
        default_factory=lambda: V1GlusterfsVolumeSource()
    )

    host_path: V1HostPathVolumeSource = Field(
        default_factory=lambda: V1HostPathVolumeSource(),
        serialization_alias="hostPath",
        validation_alias=AliasChoices("host_path", "hostPath"),
    )

    image: V1ImageVolumeSource = Field(default_factory=lambda: V1ImageVolumeSource())

    iscsi: V1ISCSIVolumeSource = Field(default_factory=lambda: V1ISCSIVolumeSource())

    name: str | None = Field(default=None)

    nfs: V1NFSVolumeSource = Field(default_factory=lambda: V1NFSVolumeSource())

    persistent_volume_claim: V1PersistentVolumeClaimVolumeSource = Field(
        default_factory=lambda: V1PersistentVolumeClaimVolumeSource(),
        serialization_alias="persistentVolumeClaim",
        validation_alias=AliasChoices(
            "persistent_volume_claim", "persistentVolumeClaim"
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

    projected: V1ProjectedVolumeSource = Field(
        default_factory=lambda: V1ProjectedVolumeSource()
    )

    quobyte: V1QuobyteVolumeSource = Field(
        default_factory=lambda: V1QuobyteVolumeSource()
    )

    rbd: V1RBDVolumeSource = Field(default_factory=lambda: V1RBDVolumeSource())

    scale_io: V1ScaleIOVolumeSource = Field(
        default_factory=lambda: V1ScaleIOVolumeSource(),
        serialization_alias="scaleIO",
        validation_alias=AliasChoices("scale_io", "scaleIO"),
    )

    secret: V1SecretVolumeSource = Field(default_factory=lambda: V1SecretVolumeSource())

    storageos: V1StorageOSVolumeSource = Field(
        default_factory=lambda: V1StorageOSVolumeSource()
    )

    vsphere_volume: V1VsphereVirtualDiskVolumeSource = Field(
        default_factory=lambda: V1VsphereVirtualDiskVolumeSource(),
        serialization_alias="vsphereVolume",
        validation_alias=AliasChoices("vsphere_volume", "vsphereVolume"),
    )
