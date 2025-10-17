from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ServiceAccountTokenProjection",)


class V1ServiceAccountTokenProjection(BaseModel):
    audience: str | None = None

    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )

    path: str | None = None
