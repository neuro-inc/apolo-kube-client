from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1NFSVolumeSource",)


class V1NFSVolumeSource(BaseModel):
    path: str | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    server: str | None = None
