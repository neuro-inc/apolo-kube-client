from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1beta1ResourcePool",)


class V1beta1ResourcePool(BaseModel):
    generation: int | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    resource_slice_count: int | None = Field(
        default=None,
        serialization_alias="resourceSliceCount",
        validation_alias=AliasChoices("resource_slice_count", "resourceSliceCount"),
        exclude_if=_exclude_if,
    )
