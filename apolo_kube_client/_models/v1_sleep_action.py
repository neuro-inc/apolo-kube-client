from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1SleepAction",)


class V1SleepAction(BaseModel):
    seconds: int | None = Field(default=None, exclude_if=_exclude_if)
