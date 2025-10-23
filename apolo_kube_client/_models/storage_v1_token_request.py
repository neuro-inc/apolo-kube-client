from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("StorageV1TokenRequest",)


class StorageV1TokenRequest(BaseModel):
    audience: str | None = Field(default=None, exclude_if=_exclude_if)

    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
        exclude_if=_exclude_if,
    )
