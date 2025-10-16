from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_delete_options import V1DeleteOptions
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Eviction",)


class V1Eviction(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    delete_options: V1DeleteOptions = Field(
        default_factory=lambda: V1DeleteOptions(), alias="deleteOptions"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )
