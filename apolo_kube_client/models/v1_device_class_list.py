from pydantic import AliasChoices, BaseModel, Field
from .v1_device_class import V1DeviceClass
from .v1_list_meta import V1ListMeta

__all__ = ("V1DeviceClassList",)


class V1DeviceClassList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1DeviceClass] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
