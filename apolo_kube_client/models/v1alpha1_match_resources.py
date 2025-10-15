from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector
from .v1alpha1_named_rule_with_operations import V1alpha1NamedRuleWithOperations


class V1alpha1MatchResources(BaseModel):
    exclude_resource_rules: list[V1alpha1NamedRuleWithOperations] | None = Field(
        None, alias="excludeResourceRules"
    )

    match_policy: str | None = Field(None, alias="matchPolicy")

    namespace_selector: V1LabelSelector | None = Field(None, alias="namespaceSelector")

    object_selector: V1LabelSelector | None = Field(None, alias="objectSelector")

    resource_rules: list[V1alpha1NamedRuleWithOperations] | None = Field(
        None, alias="resourceRules"
    )
