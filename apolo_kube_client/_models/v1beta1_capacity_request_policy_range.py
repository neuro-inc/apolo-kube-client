from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1beta1CapacityRequestPolicyRange",)


class V1beta1CapacityRequestPolicyRange(BaseModel):
    max: str | None = Field(default=None, exclude_if=_exclude_if)

    min: str | None = Field(default=None, exclude_if=_exclude_if)

    step: str | None = Field(default=None, exclude_if=_exclude_if)
