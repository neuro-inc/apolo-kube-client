from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none


__all__ = ("V1FCVolumeSource",)


class V1FCVolumeSource(BaseConfiguredModel):
    """Represents a Fibre Channel volume. Fibre Channel volumes can only be mounted as read/write once. Fibre Channel volumes support ownership management and SELinux relabeling."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.FCVolumeSource"

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    lun: Annotated[
        int | None,
        Field(
            description="""lun is Optional: FC target lun number""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    target_ww_ns: Annotated[
        list[str],
        Field(
            alias="targetWWNs",
            description="""targetWWNs is Optional: FC target worldwide names (WWNs)""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    wwids: Annotated[
        list[str],
        Field(
            description="""wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
