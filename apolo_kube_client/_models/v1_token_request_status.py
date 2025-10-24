from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1TokenRequestStatus",)


class V1TokenRequestStatus(BaseModel):
    """TokenRequestStatus is the result of a token request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authentication.v1.TokenRequestStatus"
    )

    expiration_timestamp: Annotated[
        datetime,
        Field(
            alias="expirationTimestamp",
            description="""ExpirationTimestamp is the time of expiration of the returned token.""",
        ),
    ]

    token: Annotated[str, Field(description="""Token is the opaque bearer token.""")]
