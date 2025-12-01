from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile


__all__ = ("V1DownwardAPIProjection",)


class V1DownwardAPIProjection(BaseConfiguredModel):
    """Represents downward API info for projecting into a projected volume. Note that this is identical to a downwardAPI volume source without the default mode."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.DownwardAPIProjection"

    items: Annotated[
        list[V1DownwardAPIVolumeFile],
        Field(
            description="""Items is a list of DownwardAPIVolume file""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
