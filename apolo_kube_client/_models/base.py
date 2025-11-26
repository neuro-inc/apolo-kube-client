from pydantic import BaseModel

from .v1_list_meta import V1ListMeta
from .v1_object_meta import V1ObjectMeta


class ResourceModel(BaseModel):
    metadata: V1ObjectMeta = V1ObjectMeta()


class ListModel(BaseModel):
    metadata: V1ListMeta = V1ListMeta()


class CollectionModel[T](ListModel):
    items: list[T]
