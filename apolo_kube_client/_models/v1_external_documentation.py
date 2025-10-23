from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ExternalDocumentation",)


class V1ExternalDocumentation(BaseModel):
    description: str | None = Field(default=None, exclude_if=_exclude_if)

    url: str | None = Field(default=None, exclude_if=_exclude_if)
