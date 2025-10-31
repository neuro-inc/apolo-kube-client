from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
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

__all__ = ("V1PersistentVolumeSpec",)


class V1PersistentVolumeSpec(BaseModel):
    """PersistentVolumeSpec is the specification of a persistent volume."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PersistentVolumeSpec"

    access_modes: Annotated[
        list[str],
        Field(
            alias="accessModes",
            description="""accessModes contains all ways the volume can be mounted. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    aws_elastic_block_store: Annotated[
        V1AWSElasticBlockStoreVolumeSource | None,
        Field(
            alias="awsElasticBlockStore",
            description="""awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    azure_disk: Annotated[
        V1AzureDiskVolumeSource | None,
        Field(
            alias="azureDisk",
            description="""azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    azure_file: Annotated[
        V1AzureFilePersistentVolumeSource | None,
        Field(
            alias="azureFile",
            description="""azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    capacity: Annotated[
        dict[str, str],
        Field(
            description="""capacity is the description of the persistent volume's resources and capacity. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    cephfs: Annotated[
        V1CephFSPersistentVolumeSource | None,
        Field(
            description="""cephFS represents a Ceph FS mount on the host that shares a pod's lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    cinder: Annotated[
        V1CinderPersistentVolumeSource | None,
        Field(
            description="""cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: https://examples.k8s.io/mysql-cinder-pd/README.md""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    claim_ref: Annotated[
        V1ObjectReference,
        Field(
            alias="claimRef",
            description="""claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectReference)),
    ] = V1ObjectReference()

    csi: Annotated[
        V1CSIPersistentVolumeSource | None,
        Field(
            description="""csi represents storage that is handled by an external CSI driver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    fc: Annotated[
        V1FCVolumeSource,
        Field(
            description="""fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1FCVolumeSource)),
    ] = V1FCVolumeSource()

    flex_volume: Annotated[
        V1FlexPersistentVolumeSource | None,
        Field(
            alias="flexVolume",
            description="""flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    flocker: Annotated[
        V1FlockerVolumeSource,
        Field(
            description="""flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1FlockerVolumeSource)),
    ] = V1FlockerVolumeSource()

    gce_persistent_disk: Annotated[
        V1GCEPersistentDiskVolumeSource | None,
        Field(
            alias="gcePersistentDisk",
            description="""gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    glusterfs: Annotated[
        V1GlusterfsPersistentVolumeSource | None,
        Field(
            description="""glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported. More info: https://examples.k8s.io/volumes/glusterfs/README.md""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    host_path: Annotated[
        V1HostPathVolumeSource | None,
        Field(
            alias="hostPath",
            description="""hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    iscsi: Annotated[
        V1ISCSIPersistentVolumeSource | None,
        Field(
            description="""iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    local: Annotated[
        V1LocalVolumeSource | None,
        Field(
            description="""local represents directly-attached storage with node affinity""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    mount_options: Annotated[
        list[str],
        Field(
            alias="mountOptions",
            description="""mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    nfs: Annotated[
        V1NFSVolumeSource | None,
        Field(
            description="""nfs represents an NFS mount on the host. Provisioned by an admin. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    node_affinity: Annotated[
        V1VolumeNodeAffinity,
        Field(
            alias="nodeAffinity",
            description="""nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1VolumeNodeAffinity)),
    ] = V1VolumeNodeAffinity()

    persistent_volume_reclaim_policy: Annotated[
        str | None,
        Field(
            alias="persistentVolumeReclaimPolicy",
            description="""persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    photon_persistent_disk: Annotated[
        V1PhotonPersistentDiskVolumeSource | None,
        Field(
            alias="photonPersistentDisk",
            description="""photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    portworx_volume: Annotated[
        V1PortworxVolumeSource | None,
        Field(
            alias="portworxVolume",
            description="""portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    quobyte: Annotated[
        V1QuobyteVolumeSource | None,
        Field(
            description="""quobyte represents a Quobyte mount on the host that shares a pod's lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    rbd: Annotated[
        V1RBDPersistentVolumeSource | None,
        Field(
            description="""rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported. More info: https://examples.k8s.io/volumes/rbd/README.md""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    scale_io: Annotated[
        V1ScaleIOPersistentVolumeSource | None,
        Field(
            alias="scaleIO",
            description="""scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    storage_class_name: Annotated[
        str | None,
        Field(
            alias="storageClassName",
            description="""storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    storageos: Annotated[
        V1StorageOSPersistentVolumeSource,
        Field(
            description="""storageOS represents a StorageOS volume that is attached to the kubelet's host machine and mounted into the pod. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported. More info: https://examples.k8s.io/volumes/storageos/README.md""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1StorageOSPersistentVolumeSource)),
    ] = V1StorageOSPersistentVolumeSource()

    volume_attributes_class_name: Annotated[
        str | None,
        Field(
            alias="volumeAttributesClassName",
            description="""Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_mode: Annotated[
        str | None,
        Field(
            alias="volumeMode",
            description="""volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    vsphere_volume: Annotated[
        V1VsphereVirtualDiskVolumeSource | None,
        Field(
            alias="vsphereVolume",
            description="""vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
