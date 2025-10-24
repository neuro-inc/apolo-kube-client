from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1TokenReviewSpec",)


class V1TokenReviewSpec(BaseModel):
    """TokenReviewSpec is a description of the token authentication request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authentication.v1.TokenReviewSpec"
    )

    audiences: Annotated[
        list[str],
        Field(
            description="""Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    token: Annotated[
        str | None,
        Field(
            description="""Token is the opaque bearer token.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
