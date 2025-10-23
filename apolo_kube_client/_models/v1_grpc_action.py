from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1GRPCAction",)


class V1GRPCAction(BaseModel):
    port: int | None = Field(default=None, exclude_if=_exclude_if)

    service: str | None = Field(default=None, exclude_if=_exclude_if)
