from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ResourcePool",)


class V1ResourcePool(BaseModel):
    generation: int | None = None

    name: str | None = None

    resource_slice_count: int | None = Field(
        default=None,
        serialization_alias="resourceSliceCount",
        validation_alias=AliasChoices("resource_slice_count", "resourceSliceCount"),
    )
