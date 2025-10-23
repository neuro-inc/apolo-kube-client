from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ContainerStateWaiting",)


class V1ContainerStateWaiting(BaseModel):
    message: str | None = Field(default=None, exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)
