from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("ApiregistrationV1ServiceReference",)


class ApiregistrationV1ServiceReference(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace: str | None = Field(default=None, exclude_if=_exclude_if)

    port: int | None = Field(default=None, exclude_if=_exclude_if)
