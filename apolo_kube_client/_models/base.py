from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_list_meta import V1ListMeta


class ResourceModel(BaseModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())


class ListModel(BaseModel):
    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
