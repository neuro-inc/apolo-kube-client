from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1SelfSubjectRulesReviewSpec",)


class V1SelfSubjectRulesReviewSpec(BaseModel):
    """SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.SelfSubjectRulesReviewSpec"
    )

    namespace: Annotated[
        str | None,
        Field(
            description="""Namespace to evaluate rules for. Required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
