from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_success_policy_rule import V1SuccessPolicyRule

__all__ = ("V1SuccessPolicy",)


class V1SuccessPolicy(BaseModel):
    """SuccessPolicy describes when a Job can be declared as succeeded based on the success of some indexes."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.SuccessPolicy"

    rules: Annotated[
        list[V1SuccessPolicyRule],
        Field(
            description="""rules represents the list of alternative rules for the declaring the Jobs as successful before `.status.succeeded >= .spec.completions`. Once any of the rules are met, the "SuccessCriteriaMet" condition is added, and the lingering pods are removed. The terminal state for such a Job has the "Complete" condition. Additionally, these rules are evaluated in order; Once the Job meets one of the rules, other rules are ignored. At most 20 elements are allowed."""
        ),
    ]
