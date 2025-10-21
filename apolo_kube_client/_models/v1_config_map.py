from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ConfigMap",)


class V1ConfigMap(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    binary_data: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="binaryData",
        validation_alias=AliasChoices("binary_data", "binaryData"),
    )

    data: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    immutable: bool | None = None

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())
