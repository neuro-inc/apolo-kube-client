from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1beta1_service_cidr_spec import V1beta1ServiceCIDRSpec
from .v1beta1_service_cidr_status import V1beta1ServiceCIDRStatus

__all__ = ("V1beta1ServiceCIDR",)


class V1beta1ServiceCIDR(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1beta1ServiceCIDRSpec | None = Field(None, alias="spec")

    status: V1beta1ServiceCIDRStatus | None = Field(None, alias="status")
