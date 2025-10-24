from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PhotonPersistentDiskVolumeSource",)


class V1PhotonPersistentDiskVolumeSource(BaseModel):
    """Represents a Photon Controller persistent disk resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.PhotonPersistentDiskVolumeSource"
    )

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pd_id: Annotated[
        str,
        Field(
            alias="pdID",
            description="""pdID is the ID that identifies Photon Controller persistent disk""",
        ),
    ]
