from pydantic import BaseModel, Field

from .v1_a_w_s_elastic_block_store_volume_source import (
    V1AWSElasticBlockStoreVolumeSource,
)
from .v1_azure_disk_volume_source import V1AzureDiskVolumeSource
from .v1_azure_file_persistent_volume_source import V1AzureFilePersistentVolumeSource
from .v1_c_s_i_persistent_volume_source import V1CSIPersistentVolumeSource
from .v1_ceph_f_s_persistent_volume_source import V1CephFSPersistentVolumeSource
from .v1_cinder_persistent_volume_source import V1CinderPersistentVolumeSource
from .v1_f_c_volume_source import V1FCVolumeSource
from .v1_flex_persistent_volume_source import V1FlexPersistentVolumeSource
from .v1_flocker_volume_source import V1FlockerVolumeSource
from .v1_g_c_e_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource
from .v1_glusterfs_persistent_volume_source import V1GlusterfsPersistentVolumeSource
from .v1_host_path_volume_source import V1HostPathVolumeSource
from .v1_i_s_c_s_i_persistent_volume_source import V1ISCSIPersistentVolumeSource
from .v1_local_volume_source import V1LocalVolumeSource
from .v1_n_f_s_volume_source import V1NFSVolumeSource
from .v1_object_reference import V1ObjectReference
from .v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource
from .v1_portworx_volume_source import V1PortworxVolumeSource
from .v1_quobyte_volume_source import V1QuobyteVolumeSource
from .v1_r_b_d_persistent_volume_source import V1RBDPersistentVolumeSource
from .v1_scale_i_o_persistent_volume_source import V1ScaleIOPersistentVolumeSource
from .v1_storage_o_s_persistent_volume_source import V1StorageOSPersistentVolumeSource
from .v1_volume_node_affinity import V1VolumeNodeAffinity
from .v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource


class V1PersistentVolumeSpec(BaseModel):
    access_modes: list[str] | None = Field(None, alias="accessModes")

    aws_elastic_block_store: V1AWSElasticBlockStoreVolumeSource | None = Field(
        None, alias="awsElasticBlockStore"
    )

    azure_disk: V1AzureDiskVolumeSource | None = Field(None, alias="azureDisk")

    azure_file: V1AzureFilePersistentVolumeSource | None = Field(
        None, alias="azureFile"
    )

    capacity: dict(str, str) | None = Field(None, alias="capacity")

    cephfs: V1CephFSPersistentVolumeSource | None = Field(None, alias="cephfs")

    cinder: V1CinderPersistentVolumeSource | None = Field(None, alias="cinder")

    claim_ref: V1ObjectReference | None = Field(None, alias="claimRef")

    csi: V1CSIPersistentVolumeSource | None = Field(None, alias="csi")

    fc: V1FCVolumeSource | None = Field(None, alias="fc")

    flex_volume: V1FlexPersistentVolumeSource | None = Field(None, alias="flexVolume")

    flocker: V1FlockerVolumeSource | None = Field(None, alias="flocker")

    gce_persistent_disk: V1GCEPersistentDiskVolumeSource | None = Field(
        None, alias="gcePersistentDisk"
    )

    glusterfs: V1GlusterfsPersistentVolumeSource | None = Field(None, alias="glusterfs")

    host_path: V1HostPathVolumeSource | None = Field(None, alias="hostPath")

    iscsi: V1ISCSIPersistentVolumeSource | None = Field(None, alias="iscsi")

    local: V1LocalVolumeSource | None = Field(None, alias="local")

    mount_options: list[str] | None = Field(None, alias="mountOptions")

    nfs: V1NFSVolumeSource | None = Field(None, alias="nfs")

    node_affinity: V1VolumeNodeAffinity | None = Field(None, alias="nodeAffinity")

    persistent_volume_reclaim_policy: str | None = Field(
        None, alias="persistentVolumeReclaimPolicy"
    )

    photon_persistent_disk: V1PhotonPersistentDiskVolumeSource | None = Field(
        None, alias="photonPersistentDisk"
    )

    portworx_volume: V1PortworxVolumeSource | None = Field(None, alias="portworxVolume")

    quobyte: V1QuobyteVolumeSource | None = Field(None, alias="quobyte")

    rbd: V1RBDPersistentVolumeSource | None = Field(None, alias="rbd")

    scale_io: V1ScaleIOPersistentVolumeSource | None = Field(None, alias="scaleIO")

    storage_class_name: str | None = Field(None, alias="storageClassName")

    storageos: V1StorageOSPersistentVolumeSource | None = Field(None, alias="storageos")

    volume_attributes_class_name: str | None = Field(
        None, alias="volumeAttributesClassName"
    )

    volume_mode: str | None = Field(None, alias="volumeMode")

    vsphere_volume: V1VsphereVirtualDiskVolumeSource | None = Field(
        None, alias="vsphereVolume"
    )
