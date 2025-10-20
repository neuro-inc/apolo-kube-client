from pydantic import BaseModel


__all__ = ("V1alpha1MatchCondition",)


class V1alpha1MatchCondition(BaseModel):
    expression: str | None = None

    name: str | None = None
