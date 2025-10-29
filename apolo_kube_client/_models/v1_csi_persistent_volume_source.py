from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator

__all__ = ("V1CSIPersistentVolumeSource",)


class V1CSIPersistentVolumeSource(BaseModel):
    """Represents storage that is managed by an external CSI volume driver"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.CSIPersistentVolumeSource"
    )

    controller_expand_secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="controllerExpandSecretRef",
            description="""controllerExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerExpandVolume call. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    controller_publish_secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="controllerPublishSecretRef",
            description="""controllerPublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI ControllerPublishVolume and ControllerUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    driver: Annotated[
        str,
        Field(
            description="""driver is the name of the driver to use for this volume. Required."""
        ),
    ]

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    node_expand_secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="nodeExpandSecretRef",
            description="""nodeExpandSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeExpandVolume call. This field is optional, may be omitted if no secret is required. If the secret object contains more than one secret, all secrets are passed.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    node_publish_secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="nodePublishSecretRef",
            description="""nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    node_stage_secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="nodeStageSecretRef",
            description="""nodeStageSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secrets are passed.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_attributes: Annotated[
        dict[str, str],
        Field(
            alias="volumeAttributes",
            description="""volumeAttributes of the volume to publish.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    volume_handle: Annotated[
        str,
        Field(
            alias="volumeHandle",
            description="""volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.""",
        ),
    ]
