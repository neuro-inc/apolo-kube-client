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
    aws_elastic_block_store: V1AWSElasticBlockStoreVolumeSource | None = Field(
        None, alias="awsElasticBlockStore"
    )

    azure_disk: V1AzureDiskVolumeSource | None = Field(None, alias="azureDisk")

    azure_file: V1AzureFileVolumeSource | None = Field(None, alias="azureFile")

    cephfs: V1CephFSVolumeSource | None = Field(None, alias="cephfs")

    cinder: V1CinderVolumeSource | None = Field(None, alias="cinder")

    config_map: V1ConfigMapVolumeSource | None = Field(None, alias="configMap")

    csi: V1CSIVolumeSource | None = Field(None, alias="csi")

    downward_api: V1DownwardAPIVolumeSource | None = Field(None, alias="downwardAPI")

    empty_dir: V1EmptyDirVolumeSource | None = Field(None, alias="emptyDir")

    ephemeral: V1EphemeralVolumeSource | None = Field(None, alias="ephemeral")

    fc: V1FCVolumeSource | None = Field(None, alias="fc")

    flex_volume: V1FlexVolumeSource | None = Field(None, alias="flexVolume")

    flocker: V1FlockerVolumeSource | None = Field(None, alias="flocker")

    gce_persistent_disk: V1GCEPersistentDiskVolumeSource | None = Field(
        None, alias="gcePersistentDisk"
    )

    git_repo: V1GitRepoVolumeSource | None = Field(None, alias="gitRepo")

    glusterfs: V1GlusterfsVolumeSource | None = Field(None, alias="glusterfs")

    host_path: V1HostPathVolumeSource | None = Field(None, alias="hostPath")

    image: V1ImageVolumeSource | None = Field(None, alias="image")

    iscsi: V1ISCSIVolumeSource | None = Field(None, alias="iscsi")

    name: str | None = Field(None, alias="name")

    nfs: V1NFSVolumeSource | None = Field(None, alias="nfs")

    persistent_volume_claim: V1PersistentVolumeClaimVolumeSource | None = Field(
        None, alias="persistentVolumeClaim"
    )

    photon_persistent_disk: V1PhotonPersistentDiskVolumeSource | None = Field(
        None, alias="photonPersistentDisk"
    )

    portworx_volume: V1PortworxVolumeSource | None = Field(None, alias="portworxVolume")

    projected: V1ProjectedVolumeSource | None = Field(None, alias="projected")

    quobyte: V1QuobyteVolumeSource | None = Field(None, alias="quobyte")

    rbd: V1RBDVolumeSource | None = Field(None, alias="rbd")

    scale_io: V1ScaleIOVolumeSource | None = Field(None, alias="scaleIO")

    secret: V1SecretVolumeSource | None = Field(None, alias="secret")

    storageos: V1StorageOSVolumeSource | None = Field(None, alias="storageos")

    vsphere_volume: V1VsphereVirtualDiskVolumeSource | None = Field(
        None, alias="vsphereVolume"
    )
