from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1FileKeySelector",)


class V1FileKeySelector(BaseModel):
    key: str | None = None

    optional: bool | None = None

    path: str | None = None

    volume_name: str | None = Field(
        default=None,
        serialization_alias="volumeName",
        validation_alias=AliasChoices("volume_name", "volumeName"),
    )
