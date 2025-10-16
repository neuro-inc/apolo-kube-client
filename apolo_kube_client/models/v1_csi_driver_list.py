from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_csi_driver import V1CSIDriver
from .v1_list_meta import V1ListMeta

__all__ = ("V1CSIDriverList",)


class V1CSIDriverList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1CSIDriver] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
