from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector
from .v1beta1_named_rule_with_operations import V1beta1NamedRuleWithOperations


class V1beta1MatchResources(BaseModel):
    exclude_resource_rules: list[V1beta1NamedRuleWithOperations] | None = Field(
        None, alias="excludeResourceRules"
    )

    match_policy: str | None = Field(None, alias="matchPolicy")

    namespace_selector: V1LabelSelector | None = Field(None, alias="namespaceSelector")

    object_selector: V1LabelSelector | None = Field(None, alias="objectSelector")

    resource_rules: list[V1beta1NamedRuleWithOperations] | None = Field(
        None, alias="resourceRules"
    )
