from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_non_resource_rule import V1NonResourceRule
from .v1_resource_rule import V1ResourceRule

__all__ = ("V1SubjectRulesReviewStatus",)


class V1SubjectRulesReviewStatus(BaseModel):
    """SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.SubjectRulesReviewStatus"
    )

    evaluation_error: Annotated[
        str | None,
        Field(
            alias="evaluationError",
            description="""EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    incomplete: Annotated[
        bool,
        Field(
            description="""Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation."""
        ),
    ]

    non_resource_rules: Annotated[
        list[V1NonResourceRule],
        Field(
            alias="nonResourceRules",
            description="""NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.""",
        ),
    ]

    resource_rules: Annotated[
        list[V1ResourceRule],
        Field(
            alias="resourceRules",
            description="""ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.""",
        ),
    ]
