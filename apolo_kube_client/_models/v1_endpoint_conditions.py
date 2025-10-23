from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1EndpointConditions",)


class V1EndpointConditions(BaseModel):
    ready: bool | None = Field(default=None, exclude_if=_exclude_if)

    serving: bool | None = Field(default=None, exclude_if=_exclude_if)

    terminating: bool | None = Field(default=None, exclude_if=_exclude_if)
