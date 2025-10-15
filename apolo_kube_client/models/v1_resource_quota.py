from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_resource_quota_spec import V1ResourceQuotaSpec
from .v1_resource_quota_status import V1ResourceQuotaStatus


class V1ResourceQuota(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1ResourceQuotaSpec | None = Field(None, alias="spec")

    status: V1ResourceQuotaStatus | None = Field(None, alias="status")
