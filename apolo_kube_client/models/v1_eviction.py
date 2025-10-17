from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_delete_options import V1DeleteOptions
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Eviction",)


class V1Eviction(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    delete_options: V1DeleteOptions = Field(
        default_factory=lambda: V1DeleteOptions(),
        serialization_alias="deleteOptions",
        validation_alias=AliasChoices("delete_options", "deleteOptions"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta
