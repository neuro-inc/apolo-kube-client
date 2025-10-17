from pydantic import BaseModel


__all__ = ("V1ComponentCondition",)


class V1ComponentCondition(BaseModel):
    error: str | None = None

    message: str | None = None

    status: str | None = None

    type: str | None = None
