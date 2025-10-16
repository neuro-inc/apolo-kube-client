from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_delete_options import V1DeleteOptions
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Eviction",)


class V1Eviction(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    delete_options: V1DeleteOptions | None = Field(None, alias="deleteOptions")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")
