from pydantic import BaseModel, Field

from .v1_downward_a_p_i_volume_file import V1DownwardAPIVolumeFile


class V1DownwardAPIProjection(BaseModel):
    items: list[V1DownwardAPIVolumeFile] | None = Field(None, alias="items")
