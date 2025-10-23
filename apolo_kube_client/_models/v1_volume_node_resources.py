from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1VolumeNodeResources",)


class V1VolumeNodeResources(BaseModel):
    count: int | None = Field(default=None, exclude_if=_exclude_if)
