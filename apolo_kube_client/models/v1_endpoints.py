from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_endpoint_subset import V1EndpointSubset
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Endpoints",)


class V1Endpoints(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    subsets: list[V1EndpointSubset] = Field(default=[])
