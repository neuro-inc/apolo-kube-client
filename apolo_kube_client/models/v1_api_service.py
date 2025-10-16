from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_api_service_spec import V1APIServiceSpec
from .v1_api_service_status import V1APIServiceStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1APIService",)


class V1APIService(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1APIServiceSpec | None = Field(None, alias="spec")

    status: V1APIServiceStatus | None = Field(None, alias="status")
