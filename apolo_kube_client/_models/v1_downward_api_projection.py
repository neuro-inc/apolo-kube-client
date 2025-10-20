from pydantic import BaseModel
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile

__all__ = ("V1DownwardAPIProjection",)


class V1DownwardAPIProjection(BaseModel):
    items: list[V1DownwardAPIVolumeFile] = []
