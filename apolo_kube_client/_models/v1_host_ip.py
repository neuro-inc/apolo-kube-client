from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1HostIP",)


class V1HostIP(BaseModel):
    ip: str | None = Field(default=None, exclude_if=_exclude_if)
