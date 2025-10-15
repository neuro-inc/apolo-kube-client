from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_token_request_spec import V1TokenRequestSpec
from .v1_token_request_status import V1TokenRequestStatus


class AuthenticationV1TokenRequest(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1TokenRequestSpec | None = Field(None, alias="spec")

    status: V1TokenRequestStatus | None = Field(None, alias="status")
