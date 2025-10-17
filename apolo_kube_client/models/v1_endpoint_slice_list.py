from pydantic import AliasChoices, BaseModel, Field
from .v1_endpoint_slice import V1EndpointSlice
from .v1_list_meta import V1ListMeta

__all__ = ("V1EndpointSliceList",)


class V1EndpointSliceList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1EndpointSlice] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
