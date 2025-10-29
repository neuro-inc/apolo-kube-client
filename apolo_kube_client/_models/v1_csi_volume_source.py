from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_local_object_reference import V1LocalObjectReference
from pydantic import BeforeValidator

__all__ = ("V1CSIVolumeSource",)


class V1CSIVolumeSource(BaseModel):
    """Represents a source location of a volume to mount, managed by an external CSI driver"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.CSIVolumeSource"

    driver: Annotated[
        str,
        Field(
            description="""driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster."""
        ),
    ]

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    node_publish_secret_ref: Annotated[
        V1LocalObjectReference,
        Field(
            alias="nodePublishSecretRef",
            description="""nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and  may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LocalObjectReference)),
    ] = V1LocalObjectReference()

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly specifies a read-only configuration for the volume. Defaults to false (read/write).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume_attributes: Annotated[
        dict[str, str],
        Field(
            alias="volumeAttributes",
            description="""volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}
