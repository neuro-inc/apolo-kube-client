from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_ingress import V1Ingress
from .v1_list_meta import V1ListMeta

__all__ = ("V1IngressList",)


class V1IngressList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1Ingress] = Field(default_factory=lambda: [], alias="items")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
