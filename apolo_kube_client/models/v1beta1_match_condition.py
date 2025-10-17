from pydantic import BaseModel


__all__ = ("V1beta1MatchCondition",)


class V1beta1MatchCondition(BaseModel):
    expression: str | None = None

    name: str | None = None
