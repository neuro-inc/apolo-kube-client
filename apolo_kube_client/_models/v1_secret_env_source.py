from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1SecretEnvSource",)


class V1SecretEnvSource(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    optional: bool | None = Field(default=None, exclude_if=_exclude_if)
