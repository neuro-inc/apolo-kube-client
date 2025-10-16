from __future__ import annotations
from pydantic import BaseModel, Field
from .flowcontrol_v1_subject import FlowcontrolV1Subject
from .v1_non_resource_policy_rule import V1NonResourcePolicyRule
from .v1_resource_policy_rule import V1ResourcePolicyRule

__all__ = ("V1PolicyRulesWithSubjects",)


class V1PolicyRulesWithSubjects(BaseModel):
    non_resource_rules: list[V1NonResourcePolicyRule] = Field(
        default_factory=lambda: [], alias="nonResourceRules"
    )

    resource_rules: list[V1ResourcePolicyRule] = Field(
        default_factory=lambda: [], alias="resourceRules"
    )

    subjects: list[FlowcontrolV1Subject] = Field(
        default_factory=lambda: [], alias="subjects"
    )
