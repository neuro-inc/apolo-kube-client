from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_config_source import V1NodeConfigSource
from .v1_taint import V1Taint

__all__ = ("V1NodeSpec",)


class V1NodeSpec(BaseModel):
    config_source: V1NodeConfigSource = Field(
        default_factory=lambda: V1NodeConfigSource(), alias="configSource"
    )

    external_id: str | None = Field(default_factory=lambda: None, alias="externalID")

    pod_cidr: str | None = Field(default_factory=lambda: None, alias="podCIDR")

    pod_cid_rs: list[str] = Field(default_factory=lambda: [], alias="podCIDRs")

    provider_id: str | None = Field(default_factory=lambda: None, alias="providerID")

    taints: list[V1Taint] = Field(default_factory=lambda: [], alias="taints")

    unschedulable: bool | None = Field(
        default_factory=lambda: None, alias="unschedulable"
    )
