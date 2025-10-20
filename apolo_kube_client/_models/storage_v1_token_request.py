from pydantic import AliasChoices, BaseModel, Field


__all__ = ("StorageV1TokenRequest",)


class StorageV1TokenRequest(BaseModel):
    audience: str | None = None

    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )
