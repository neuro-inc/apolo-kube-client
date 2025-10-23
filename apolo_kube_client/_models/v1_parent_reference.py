from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ParentReference",)


class V1ParentReference(BaseModel):
    group: str | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace: str | None = Field(default=None, exclude_if=_exclude_if)

    resource: str | None = Field(default=None, exclude_if=_exclude_if)
