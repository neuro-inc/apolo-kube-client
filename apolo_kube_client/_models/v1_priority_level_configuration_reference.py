from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PriorityLevelConfigurationReference",)


class V1PriorityLevelConfigurationReference(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)
