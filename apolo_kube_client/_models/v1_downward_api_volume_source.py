from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile
from pydantic import BeforeValidator

__all__ = ("V1DownwardAPIVolumeSource",)


class V1DownwardAPIVolumeSource(BaseModel):
    """DownwardAPIVolumeSource represents a volume containing downward API info. Downward API volumes support ownership management and SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.DownwardAPIVolumeSource"

    default_mode: Annotated[
        int | None,
        Field(
            alias="defaultMode",
            description="""Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    items: Annotated[
        list[V1DownwardAPIVolumeFile],
        Field(
            description="""Items is a list of downward API volume file""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
