from pydantic import BaseModel, Field

from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector


class V1DownwardAPIVolumeFile(BaseModel):
    field_ref: V1ObjectFieldSelector | None = Field(None, alias="fieldRef")

    mode: int | None = Field(None, alias="mode")

    path: str | None = Field(None, alias="path")

    resource_field_ref: V1ResourceFieldSelector | None = Field(
        None, alias="resourceFieldRef"
    )
