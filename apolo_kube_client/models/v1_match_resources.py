from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_named_rule_with_operations import V1NamedRuleWithOperations

__all__ = ("V1MatchResources",)


class V1MatchResources(BaseModel):
    exclude_resource_rules: list[V1NamedRuleWithOperations] = Field(
        default_factory=lambda: [], alias="excludeResourceRules"
    )

    match_policy: str | None = Field(default_factory=lambda: None, alias="matchPolicy")

    namespace_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="namespaceSelector"
    )

    object_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="objectSelector"
    )

    resource_rules: list[V1NamedRuleWithOperations] = Field(
        default_factory=lambda: [], alias="resourceRules"
    )
