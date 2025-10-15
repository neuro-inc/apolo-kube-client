from pydantic import BaseModel, Field


class V1alpha3ResourcePool(BaseModel):
    generation: int | None = Field(None, alias="generation")

    name: str | None = Field(None, alias="name")

    resource_slice_count: int | None = Field(None, alias="resourceSliceCount")
