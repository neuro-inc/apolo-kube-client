from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ContainerImage",)


class V1ContainerImage(BaseModel):
    names: list[str] = []

    size_bytes: int | None = Field(
        default=None,
        serialization_alias="sizeBytes",
        validation_alias=AliasChoices("size_bytes", "sizeBytes"),
    )
