from pydantic import BaseModel, ConfigDict

from .v1_list_meta import V1ListMeta
from .v1_object_meta import V1ObjectMeta


class BaseConfiguredModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )


class ResourceModel(BaseConfiguredModel):
    metadata: V1ObjectMeta = V1ObjectMeta()


class ListModel(BaseConfiguredModel):
    metadata: V1ListMeta = V1ListMeta()


class CollectionModel[T](ListModel):
    items: list[T]
