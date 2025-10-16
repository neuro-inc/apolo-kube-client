from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_node_selector import V1NodeSelector
from .v1alpha3_device import V1alpha3Device
from .v1alpha3_resource_pool import V1alpha3ResourcePool

__all__ = ("V1alpha3ResourceSliceSpec",)


class V1alpha3ResourceSliceSpec(BaseModel):
    all_nodes: bool | None = Field(None, alias="allNodes")

    devices: list[V1alpha3Device] | None = Field(None, alias="devices")

    driver: str | None = Field(None, alias="driver")

    node_name: str | None = Field(None, alias="nodeName")

    node_selector: V1NodeSelector | None = Field(None, alias="nodeSelector")

    pool: V1alpha3ResourcePool | None = Field(None, alias="pool")
