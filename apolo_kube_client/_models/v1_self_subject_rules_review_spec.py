from pydantic import BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1SelfSubjectRulesReviewSpec",)


class V1SelfSubjectRulesReviewSpec(BaseModel):
    namespace: str | None = Field(default=None, exclude_if=_exclude_if)
