from pydantic import BaseModel


__all__ = ("V1StatusCause",)


class V1StatusCause(BaseModel):
    field: str | None = None

    message: str | None = None

    reason: str | None = None
