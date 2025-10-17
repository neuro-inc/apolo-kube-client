from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_resource_quota_spec import V1ResourceQuotaSpec
from .v1_resource_quota_status import V1ResourceQuotaStatus

__all__ = ("V1ResourceQuota",)


class V1ResourceQuota(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1ResourceQuotaSpec = Field(default_factory=lambda: V1ResourceQuotaSpec())

    status: V1ResourceQuotaStatus = Field(
        default_factory=lambda: V1ResourceQuotaStatus()
    )
