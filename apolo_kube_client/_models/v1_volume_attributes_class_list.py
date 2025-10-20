from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1_volume_attributes_class import V1VolumeAttributesClass

__all__ = ("V1VolumeAttributesClassList",)


class V1VolumeAttributesClassList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1VolumeAttributesClass] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
