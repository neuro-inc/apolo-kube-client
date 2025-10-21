from pydantic import AliasChoices, Field
from .base import ListModel
from .base import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1_volume_attributes_class import V1VolumeAttributesClass
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeAttributesClassList",)


class V1VolumeAttributesClassList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1VolumeAttributesClass] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
