from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha3_device_class import V1alpha3DeviceClass

__all__ = ("V1alpha3DeviceClassList",)


class V1alpha3DeviceClassList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha3DeviceClass] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
