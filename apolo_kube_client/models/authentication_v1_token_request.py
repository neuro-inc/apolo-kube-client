from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_token_request_spec import V1TokenRequestSpec
from .v1_token_request_status import V1TokenRequestStatus

__all__ = ("AuthenticationV1TokenRequest",)


class AuthenticationV1TokenRequest(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1TokenRequestSpec = Field(default_factory=lambda: V1TokenRequestSpec())

    status: V1TokenRequestStatus = Field(default_factory=lambda: V1TokenRequestStatus())
