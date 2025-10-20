from pydantic import BaseModel


__all__ = ("V1SelfSubjectRulesReviewSpec",)


class V1SelfSubjectRulesReviewSpec(BaseModel):
    namespace: str | None = None
