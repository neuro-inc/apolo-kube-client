from pydantic import AliasChoices, BaseModel, Field
from .flowcontrol_v1_subject import FlowcontrolV1Subject
from .utils import _collection_if_none
from .v1_non_resource_policy_rule import V1NonResourcePolicyRule
from .v1_resource_policy_rule import V1ResourcePolicyRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PolicyRulesWithSubjects",)


class V1PolicyRulesWithSubjects(BaseModel):
    non_resource_rules: Annotated[
        list[V1NonResourcePolicyRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="nonResourceRules",
        validation_alias=AliasChoices("non_resource_rules", "nonResourceRules"),
    )

    resource_rules: Annotated[
        list[V1ResourcePolicyRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="resourceRules",
        validation_alias=AliasChoices("resource_rules", "resourceRules"),
    )

    subjects: Annotated[
        list[FlowcontrolV1Subject], BeforeValidator(_collection_if_none("[]"))
    ] = []
