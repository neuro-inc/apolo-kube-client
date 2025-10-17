from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1QuobyteVolumeSource",)


class V1QuobyteVolumeSource(BaseModel):
    group: str | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    registry: str | None = None

    tenant: str | None = None

    user: str | None = None

    volume: str | None = None
