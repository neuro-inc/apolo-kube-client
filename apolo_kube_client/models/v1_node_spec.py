from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_node_config_source import V1NodeConfigSource
from .v1_taint import V1Taint

__all__ = ("V1NodeSpec",)


class V1NodeSpec(BaseModel):
    config_source: V1NodeConfigSource | None = Field(None, alias="configSource")

    external_id: str | None = Field(None, alias="externalID")

    pod_cidr: str | None = Field(None, alias="podCIDR")

    pod_cid_rs: list[str] | None = Field(None, alias="podCIDRs")

    provider_id: str | None = Field(None, alias="providerID")

    taints: list[V1Taint] | None = Field(None, alias="taints")

    unschedulable: bool | None = Field(None, alias="unschedulable")
