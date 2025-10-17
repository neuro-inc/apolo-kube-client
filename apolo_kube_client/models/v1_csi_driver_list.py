from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_csi_driver import V1CSIDriver
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSIDriverList",)


class V1CSIDriverList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1CSIDriver] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
