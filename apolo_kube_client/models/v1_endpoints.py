from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_endpoint_subset import V1EndpointSubset
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Endpoints",)


class V1Endpoints(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    subsets: list[V1EndpointSubset] | None = Field(None, alias="subsets")
