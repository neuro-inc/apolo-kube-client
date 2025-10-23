from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    param_ref: Annotated[V1ParamRef, BeforeValidator(_default_if_none(V1ParamRef))] = (
        Field(
            default_factory=lambda: V1ParamRef(),
            serialization_alias="paramRef",
            validation_alias=AliasChoices("param_ref", "paramRef"),
            exclude_if=_exclude_if,
        )
    )

    policy_name: str | None = Field(
        default=None,
        serialization_alias="policyName",
        validation_alias=AliasChoices("policy_name", "policyName"),
        exclude_if=_exclude_if,
    )

    validation_actions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="validationActions",
        validation_alias=AliasChoices("validation_actions", "validationActions"),
        exclude_if=_exclude_if,
    )
