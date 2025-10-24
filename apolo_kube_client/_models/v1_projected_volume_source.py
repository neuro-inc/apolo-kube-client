from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_volume_projection import V1VolumeProjection
from pydantic import BeforeValidator

__all__ = ("V1ProjectedVolumeSource",)


class V1ProjectedVolumeSource(BaseModel):
    """Represents a projected volume source"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ProjectedVolumeSource"

    default_mode: Annotated[
        int | None,
        Field(
            alias="defaultMode",
            description="""defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    sources: Annotated[
        list[V1VolumeProjection],
        Field(
            description="""sources is the list of volume projections. Each entry in this list handles one source.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
