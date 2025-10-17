from pydantic import AliasChoices, BaseModel, Field
from .v1_csi_storage_capacity import V1CSIStorageCapacity
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSIStorageCapacityList",)


class V1CSIStorageCapacityList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CSIStorageCapacity] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
