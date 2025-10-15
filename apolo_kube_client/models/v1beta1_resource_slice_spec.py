from pydantic import BaseModel, Field

from .v1_node_selector import V1NodeSelector
from .v1beta1_device import V1beta1Device
from .v1beta1_resource_pool import V1beta1ResourcePool


class V1beta1ResourceSliceSpec(BaseModel):
    all_nodes: bool | None = Field(None, alias="allNodes")

    devices: list[V1beta1Device] | None = Field(None, alias="devices")

    driver: str | None = Field(None, alias="driver")

    node_name: str | None = Field(None, alias="nodeName")

    node_selector: V1NodeSelector | None = Field(None, alias="nodeSelector")

    pool: V1beta1ResourcePool | None = Field(None, alias="pool")
