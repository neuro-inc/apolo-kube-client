from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ScaleStatus",)


class V1ScaleStatus(BaseModel):
    replicas: int | None = Field(default=None, exclude_if=_exclude_if)

    selector: str | None = Field(default=None, exclude_if=_exclude_if)
