from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_user_info import V1UserInfo
from pydantic import BeforeValidator

__all__ = ("V1TokenReviewStatus",)


class V1TokenReviewStatus(BaseModel):
    """TokenReviewStatus is the result of the token authentication request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authentication.v1.TokenReviewStatus"
    )

    audiences: Annotated[
        list[str],
        Field(
            description="""Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token's audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    authenticated: Annotated[
        bool | None,
        Field(
            description="""Authenticated indicates that the token was associated with a known user.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    error: Annotated[
        str | None,
        Field(
            description="""Error indicates that the token couldn't be checked""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    user: Annotated[
        V1UserInfo,
        Field(
            description="""User is the UserInfo associated with the provided token.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1UserInfo)),
    ] = V1UserInfo()
