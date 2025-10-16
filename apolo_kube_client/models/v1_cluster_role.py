from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_aggregation_rule import V1AggregationRule
from .v1_object_meta import V1ObjectMeta
from .v1_policy_rule import V1PolicyRule

__all__ = ("V1ClusterRole",)


class V1ClusterRole(BaseModel):
    aggregation_rule: V1AggregationRule = Field(
        default_factory=lambda: V1AggregationRule(), alias="aggregationRule"
    )

    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    rules: list[V1PolicyRule] = Field(default_factory=lambda: [], alias="rules")
