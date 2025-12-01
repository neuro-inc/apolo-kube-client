from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1SelfSubjectRulesReviewSpec",)


class V1SelfSubjectRulesReviewSpec(BaseConfiguredModel):
    """SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview."""

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
