from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_downward_api_volume_file import V1DownwardAPIVolumeFile
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DownwardAPIProjection",)


class V1DownwardAPIProjection(BaseModel):
    items: Annotated[
        list[V1DownwardAPIVolumeFile], BeforeValidator(_collection_if_none("[]"))
    ] = []
