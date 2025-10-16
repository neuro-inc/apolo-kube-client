from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_service_cidr_spec import V1ServiceCIDRSpec
from .v1_service_cidr_status import V1ServiceCIDRStatus

__all__ = ("V1ServiceCIDR",)


class V1ServiceCIDR(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1ServiceCIDRSpec = Field(
        default_factory=lambda: V1ServiceCIDRSpec(), alias="spec"
    )

    status: V1ServiceCIDRStatus = Field(
        default_factory=lambda: V1ServiceCIDRStatus(), alias="status"
    )
