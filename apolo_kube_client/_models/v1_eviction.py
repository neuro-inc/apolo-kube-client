from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_delete_options import V1DeleteOptions
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Eviction",)


class V1Eviction(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    delete_options: Annotated[
        V1DeleteOptions, BeforeValidator(_default_if_none(V1DeleteOptions))
    ] = Field(
        default_factory=lambda: V1DeleteOptions(),
        serialization_alias="deleteOptions",
        validation_alias=AliasChoices("delete_options", "deleteOptions"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())
