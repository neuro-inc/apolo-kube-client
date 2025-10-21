from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_policy_rule import V1PolicyRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Role",)


class V1Role(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    rules: Annotated[
        list[V1PolicyRule], BeforeValidator(_collection_if_none("[]"))
    ] = []
