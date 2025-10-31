from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
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
from pydantic import BeforeValidator

__all__ = ("V1Volume",)


class V1Volume(BaseModel):
    """Volume represents a named volume in a pod that may be accessed by any container in the pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Volume"

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
        V1AzureFileVolumeSource | None,
        Field(
            alias="azureFile",
            description="""azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    cephfs: Annotated[
        V1CephFSVolumeSource | None,
        Field(
            description="""cephFS represents a Ceph FS mount on the host that shares a pod's lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    cinder: Annotated[
        V1CinderVolumeSource | None,
        Field(
            description="""cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: https://examples.k8s.io/mysql-cinder-pd/README.md""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    config_map: Annotated[
        V1ConfigMapVolumeSource,
        Field(
            alias="configMap",
            description="""configMap represents a configMap that should populate this volume""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ConfigMapVolumeSource)),
    ] = V1ConfigMapVolumeSource()

    csi: Annotated[
        V1CSIVolumeSource | None,
        Field(
            description="""csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    downward_api: Annotated[
        V1DownwardAPIVolumeSource,
        Field(
            alias="downwardAPI",
            description="""downwardAPI represents downward API about the pod that should populate this volume""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1DownwardAPIVolumeSource)),
    ] = V1DownwardAPIVolumeSource()

    empty_dir: Annotated[
        V1EmptyDirVolumeSource,
        Field(
            alias="emptyDir",
            description="""emptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1EmptyDirVolumeSource)),
    ] = V1EmptyDirVolumeSource()

    ephemeral: Annotated[
        V1EphemeralVolumeSource,
        Field(
            description="""ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.

Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity
   tracking are needed,
c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through
   a PersistentVolumeClaim (see EphemeralVolumeSource for more
   information on the connection between this volume type
   and PersistentVolumeClaim).

Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.

Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.

A pod can use both types of ephemeral volumes and persistent volumes at the same time.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1EphemeralVolumeSource)),
    ] = V1EphemeralVolumeSource()

    fc: Annotated[
        V1FCVolumeSource,
        Field(
            description="""fc represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1FCVolumeSource)),
    ] = V1FCVolumeSource()

    flex_volume: Annotated[
        V1FlexVolumeSource | None,
        Field(
            alias="flexVolume",
            description="""flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    flocker: Annotated[
        V1FlockerVolumeSource,
        Field(
            description="""flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1FlockerVolumeSource)),
    ] = V1FlockerVolumeSource()

    gce_persistent_disk: Annotated[
        V1GCEPersistentDiskVolumeSource | None,
        Field(
            alias="gcePersistentDisk",
            description="""gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    git_repo: Annotated[
        V1GitRepoVolumeSource | None,
        Field(
            alias="gitRepo",
            description="""gitRepo represents a git repository at a particular revision. Deprecated: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    glusterfs: Annotated[
        V1GlusterfsVolumeSource | None,
        Field(
            description="""glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    host_path: Annotated[
        V1HostPathVolumeSource | None,
        Field(
            alias="hostPath",
            description="""hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    image: Annotated[
        V1ImageVolumeSource,
        Field(
            description="""image represents an OCI object (a container image or artifact) pulled and mounted on the kubelet's host machine. The volume is resolved at pod startup depending on which PullPolicy value is provided:

- Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. - Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn't present. - IfNotPresent: the kubelet pulls if the reference isn't already present on disk. Container creation will fail if the reference isn't present and the pull fails.

The volume gets re-resolved if the pod gets deleted and recreated, which means that new remote content will become available on pod recreation. A failure to resolve or pull the image during pod startup will block containers from starting and may add significant latency. Failures will be retried using normal volume backoff and will be reported on the pod reason and message. The types of objects that may be mounted by this volume are defined by the container runtime implementation on a host machine and at minimum must include all valid types supported by the container image field. The OCI object gets mounted in a single directory (spec.containers[*].volumeMounts.mountPath) by merging the manifest layers in the same way as for container images. The volume will be mounted read-only (ro) and non-executable files (noexec). Sub path mounts for containers are not supported (spec.containers[*].volumeMounts.subpath) before 1.33. The field spec.securityContext.fsGroupChangePolicy has no effect on this volume type.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ImageVolumeSource)),
    ] = V1ImageVolumeSource()

    iscsi: Annotated[
        V1ISCSIVolumeSource | None,
        Field(
            description="""iscsi represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes/#iscsi""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str,
        Field(
            description="""name of the volume. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names"""
        ),
    ]

    nfs: Annotated[
        V1NFSVolumeSource | None,
        Field(
            description="""nfs represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    persistent_volume_claim: Annotated[
        V1PersistentVolumeClaimVolumeSource | None,
        Field(
            alias="persistentVolumeClaim",
            description="""persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims""",
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

    projected: Annotated[
        V1ProjectedVolumeSource,
        Field(
            description="""projected items for all in one resources secrets, configmaps, and downward API""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ProjectedVolumeSource)),
    ] = V1ProjectedVolumeSource()

    quobyte: Annotated[
        V1QuobyteVolumeSource | None,
        Field(
            description="""quobyte represents a Quobyte mount on the host that shares a pod's lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    rbd: Annotated[
        V1RBDVolumeSource | None,
        Field(
            description="""rbd represents a Rados Block Device mount on the host that shares a pod's lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    scale_io: Annotated[
        V1ScaleIOVolumeSource | None,
        Field(
            alias="scaleIO",
            description="""scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret: Annotated[
        V1SecretVolumeSource,
        Field(
            description="""secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretVolumeSource)),
    ] = V1SecretVolumeSource()

    storageos: Annotated[
        V1StorageOSVolumeSource,
        Field(
            description="""storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1StorageOSVolumeSource)),
    ] = V1StorageOSVolumeSource()

    vsphere_volume: Annotated[
        V1VsphereVirtualDiskVolumeSource | None,
        Field(
            alias="vsphereVolume",
            description="""vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
