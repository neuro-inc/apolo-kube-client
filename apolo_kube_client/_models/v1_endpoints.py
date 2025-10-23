from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_endpoint_subset import V1EndpointSubset
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Endpoints",)


class V1Endpoints(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    subsets: Annotated[
        list[V1EndpointSubset], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
