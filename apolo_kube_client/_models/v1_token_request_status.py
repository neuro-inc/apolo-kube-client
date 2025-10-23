from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1TokenRequestStatus",)


class V1TokenRequestStatus(BaseModel):
    expiration_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="expirationTimestamp",
        validation_alias=AliasChoices("expiration_timestamp", "expirationTimestamp"),
        exclude_if=_exclude_if,
    )

    token: str | None = Field(default=None, exclude_if=_exclude_if)
