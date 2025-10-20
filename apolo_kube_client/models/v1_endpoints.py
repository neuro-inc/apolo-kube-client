from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_endpoint_subset import V1EndpointSubset
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Endpoints",)


class V1Endpoints(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    subsets: list[V1EndpointSubset] = []
