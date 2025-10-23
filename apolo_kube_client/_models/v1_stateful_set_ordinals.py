from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1StatefulSetOrdinals",)


class V1StatefulSetOrdinals(BaseModel):
    start: int | None = Field(default=None, exclude_if=_exclude_if)
