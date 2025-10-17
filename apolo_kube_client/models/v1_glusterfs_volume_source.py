from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1GlusterfsVolumeSource",)


class V1GlusterfsVolumeSource(BaseModel):
    endpoints: str | None = None

    path: str | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )
