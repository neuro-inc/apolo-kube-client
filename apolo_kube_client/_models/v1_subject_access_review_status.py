from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1SubjectAccessReviewStatus",)


class V1SubjectAccessReviewStatus(BaseModel):
    """SubjectAccessReviewStatus"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.SubjectAccessReviewStatus"
    )

    allowed: Annotated[
        bool,
        Field(
            description="""Allowed is required. True if the action would be allowed, false otherwise."""
        ),
    ]

    denied: Annotated[
        bool | None,
        Field(
            description="""Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    evaluation_error: Annotated[
        str | None,
        Field(
            alias="evaluationError",
            description="""EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""Reason is optional.  It indicates why a request was allowed or denied.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
