from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_token_request_spec import V1TokenRequestSpec
from .v1_token_request_status import V1TokenRequestStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("AuthenticationV1TokenRequest",)


class AuthenticationV1TokenRequest(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1TokenRequestSpec, BeforeValidator(_default_if_none(V1TokenRequestSpec))
    ] = Field(default_factory=lambda: V1TokenRequestSpec())

    status: Annotated[
        V1TokenRequestStatus, BeforeValidator(_default_if_none(V1TokenRequestStatus))
    ] = Field(default_factory=lambda: V1TokenRequestStatus())
