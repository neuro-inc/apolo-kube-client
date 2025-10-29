from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_param_ref import V1alpha1ParamRef
from pydantic import BeforeValidator

__all__ = ("V1alpha1MutatingAdmissionPolicyBindingSpec",)


class V1alpha1MutatingAdmissionPolicyBindingSpec(BaseModel):
    """MutatingAdmissionPolicyBindingSpec is the specification of the MutatingAdmissionPolicyBinding."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1alpha1.MutatingAdmissionPolicyBindingSpec"
    )

    match_resources: Annotated[
        V1alpha1MatchResources,
        Field(
            alias="matchResources",
            description="""matchResources limits what resources match this binding and may be mutated by it. Note that if matchResources matches a resource, the resource must also match a policy's matchConstraints and matchConditions before the resource may be mutated. When matchResources is unset, it does not constrain resource matching, and only the policy's matchConstraints and matchConditions must match for the resource to be mutated. Additionally, matchResources.resourceRules are optional and do not constraint matching when unset. Note that this is differs from MutatingAdmissionPolicy matchConstraints, where resourceRules are required. The CREATE, UPDATE and CONNECT operations are allowed.  The DELETE operation may not be matched. '*' matches CREATE, UPDATE and CONNECT.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1alpha1MatchResources)),
    ] = V1alpha1MatchResources()

    param_ref: Annotated[
        V1alpha1ParamRef,
        Field(
            alias="paramRef",
            description="""paramRef specifies the parameter resource used to configure the admission control policy. It should point to a resource of the type specified in spec.ParamKind of the bound MutatingAdmissionPolicy. If the policy specifies a ParamKind and the resource referred to by ParamRef does not exist, this binding is considered mis-configured and the FailurePolicy of the MutatingAdmissionPolicy applied. If the policy does not specify a ParamKind then this field is ignored, and the rules are evaluated without a param.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1alpha1ParamRef)),
    ] = V1alpha1ParamRef()

    policy_name: Annotated[
        str | None,
        Field(
            alias="policyName",
            description="""policyName references a MutatingAdmissionPolicy name which the MutatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
