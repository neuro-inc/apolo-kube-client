from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .flowcontrol_v1_subject import FlowcontrolV1Subject
from .utils import _collection_if_none
from .v1_non_resource_policy_rule import V1NonResourcePolicyRule
from .v1_resource_policy_rule import V1ResourcePolicyRule
from pydantic import BeforeValidator

__all__ = ("V1PolicyRulesWithSubjects",)


class V1PolicyRulesWithSubjects(BaseModel):
    """PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.PolicyRulesWithSubjects"
    )

    non_resource_rules: Annotated[
        list[V1NonResourcePolicyRule],
        Field(
            alias="nonResourceRules",
            description="""`nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resource_rules: Annotated[
        list[V1ResourcePolicyRule],
        Field(
            alias="resourceRules",
            description="""`resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    subjects: Annotated[
        list[FlowcontrolV1Subject],
        Field(
            description="""subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required."""
        ),
    ]
