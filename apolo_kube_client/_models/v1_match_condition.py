from pydantic import BaseModel


__all__ = ("V1MatchCondition",)


class V1MatchCondition(BaseModel):
    expression: str | None = None

    name: str | None = None
