from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_match_resources import V1MatchResources
from .v1_param_ref import V1ParamRef
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingAdmissionPolicyBindingSpec",)


class V1ValidatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: Annotated[
        V1MatchResources, BeforeValidator(_default_if_none(V1MatchResources))
    ] = Field(
        default_factory=lambda: V1MatchResources(),
        serialization_alias="matchResources",
        validation_alias=AliasChoices("match_resources", "matchResources"),
    )

    param_ref: Annotated[V1ParamRef, BeforeValidator(_default_if_none(V1ParamRef))] = (
        Field(
            default_factory=lambda: V1ParamRef(),
            serialization_alias="paramRef",
            validation_alias=AliasChoices("param_ref", "paramRef"),
        )
    )

    policy_name: str | None = Field(
        default=None,
        serialization_alias="policyName",
        validation_alias=AliasChoices("policy_name", "policyName"),
    )

    validation_actions: list[str] = Field(
        default=[],
        serialization_alias="validationActions",
        validation_alias=AliasChoices("validation_actions", "validationActions"),
    )
