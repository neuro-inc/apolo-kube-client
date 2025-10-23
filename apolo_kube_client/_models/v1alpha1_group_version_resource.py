from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1alpha1GroupVersionResource",)


class V1alpha1GroupVersionResource(BaseModel):
    group: str | None = Field(default=None, exclude_if=_exclude_if)

    resource: str | None = Field(default=None, exclude_if=_exclude_if)

    version: str | None = Field(default=None, exclude_if=_exclude_if)
