from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_local_object_reference import V1LocalObjectReference
from pydantic import BeforeValidator

__all__ = ("V1StorageOSVolumeSource",)


class V1StorageOSVolumeSource(BaseModel):
    """Represents a StorageOS persistent volume resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.StorageOSVolumeSource"

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_ref: Annotated[
        V1LocalObjectReference,
        Field(
            alias="secretRef",
            description="""secretRef specifies the secret to use for obtaining the StorageOS API credentials.  If not specified, default values will be attempted.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LocalObjectReference)),
    ] = V1LocalObjectReference()

    volume_name: Annotated[
        str | None,
        Field(
            alias="volumeName",
            description="""volumeName is the human-readable name of the StorageOS volume.  Volume names are only unique within a namespace.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_namespace: Annotated[
        str | None,
        Field(
            alias="volumeNamespace",
            description="""volumeNamespace specifies the scope of the volume within StorageOS.  If no namespace is specified then the Pod's namespace will be used.  This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
