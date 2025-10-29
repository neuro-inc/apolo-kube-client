from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_bound_object_reference import V1BoundObjectReference
from pydantic import BeforeValidator

__all__ = ("V1TokenRequestSpec",)


class V1TokenRequestSpec(BaseModel):
    """TokenRequestSpec contains client provided parameters of a token request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authentication.v1.TokenRequestSpec"
    )

    audiences: Annotated[
        list[str],
        Field(
            description="""Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences."""
        ),
    ]

    bound_object_ref: Annotated[
        V1BoundObjectReference,
        Field(
            alias="boundObjectRef",
            description="""BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1BoundObjectReference)),
    ] = V1BoundObjectReference()

    expiration_seconds: Annotated[
        int | None,
        Field(
            alias="expirationSeconds",
            description="""ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
