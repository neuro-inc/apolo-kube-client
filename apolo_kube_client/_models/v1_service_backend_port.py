from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ServiceBackendPort",)


class V1ServiceBackendPort(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    number: int | None = Field(default=None, exclude_if=_exclude_if)
