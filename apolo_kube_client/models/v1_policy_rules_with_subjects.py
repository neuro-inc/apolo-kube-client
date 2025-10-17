from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .flowcontrol_v1_subject import FlowcontrolV1Subject
from .v1_non_resource_policy_rule import V1NonResourcePolicyRule
from .v1_resource_policy_rule import V1ResourcePolicyRule

__all__ = ("V1PolicyRulesWithSubjects",)


class V1PolicyRulesWithSubjects(BaseModel):
    non_resource_rules: list[V1NonResourcePolicyRule] = Field(
        default=[],
        serialization_alias="nonResourceRules",
        validation_alias=AliasChoices("non_resource_rules", "nonResourceRules"),
    )

    resource_rules: list[V1ResourcePolicyRule] = Field(
        default=[],
        serialization_alias="resourceRules",
        validation_alias=AliasChoices("resource_rules", "resourceRules"),
    )

    subjects: list[FlowcontrolV1Subject] = Field(default=[])
