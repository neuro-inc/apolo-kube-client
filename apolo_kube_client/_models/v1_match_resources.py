from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_label_selector import V1LabelSelector
from .v1_named_rule_with_operations import V1NamedRuleWithOperations
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1MatchResources",)


class V1MatchResources(BaseModel):
    exclude_resource_rules: Annotated[
        list[V1NamedRuleWithOperations], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="excludeResourceRules",
        validation_alias=AliasChoices("exclude_resource_rules", "excludeResourceRules"),
        exclude_if=_exclude_if,
    )

    match_policy: str | None = Field(
        default=None,
        serialization_alias="matchPolicy",
        validation_alias=AliasChoices("match_policy", "matchPolicy"),
        exclude_if=_exclude_if,
    )

    namespace_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
        exclude_if=_exclude_if,
    )

    object_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="objectSelector",
        validation_alias=AliasChoices("object_selector", "objectSelector"),
        exclude_if=_exclude_if,
    )

    resource_rules: Annotated[
        list[V1NamedRuleWithOperations], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="resourceRules",
        validation_alias=AliasChoices("resource_rules", "resourceRules"),
        exclude_if=_exclude_if,
    )
