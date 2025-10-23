from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_aggregation_rule import V1AggregationRule
from .v1_object_meta import V1ObjectMeta
from .v1_policy_rule import V1PolicyRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ClusterRole",)


class V1ClusterRole(ResourceModel):
    aggregation_rule: Annotated[
        V1AggregationRule, BeforeValidator(_default_if_none(V1AggregationRule))
    ] = Field(
        default_factory=lambda: V1AggregationRule(),
        serialization_alias="aggregationRule",
        validation_alias=AliasChoices("aggregation_rule", "aggregationRule"),
        exclude_if=_exclude_if,
    )

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

    rules: Annotated[list[V1PolicyRule], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )
