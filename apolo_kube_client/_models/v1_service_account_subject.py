from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ServiceAccountSubject",)


class V1ServiceAccountSubject(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace: str | None = Field(default=None, exclude_if=_exclude_if)
