from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_lease_spec import V1LeaseSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Lease",)


class V1Lease(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1LeaseSpec | None = Field(None, alias="spec")
