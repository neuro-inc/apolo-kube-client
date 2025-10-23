from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1GitRepoVolumeSource",)


class V1GitRepoVolumeSource(BaseModel):
    directory: str | None = Field(default=None, exclude_if=_exclude_if)

    repository: str | None = Field(default=None, exclude_if=_exclude_if)

    revision: str | None = Field(default=None, exclude_if=_exclude_if)
