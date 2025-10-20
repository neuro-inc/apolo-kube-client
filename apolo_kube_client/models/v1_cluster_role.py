from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_aggregation_rule import V1AggregationRule
from .v1_object_meta import V1ObjectMeta
from .v1_policy_rule import V1PolicyRule

__all__ = ("V1ClusterRole",)


class V1ClusterRole(ResourceModel):
    aggregation_rule: V1AggregationRule = Field(
        default_factory=lambda: V1AggregationRule(),
        serialization_alias="aggregationRule",
        validation_alias=AliasChoices("aggregation_rule", "aggregationRule"),
    )

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    rules: list[V1PolicyRule] = []
