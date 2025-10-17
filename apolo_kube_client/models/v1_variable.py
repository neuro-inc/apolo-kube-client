from pydantic import BaseModel


__all__ = ("V1Variable",)


class V1Variable(BaseModel):
    expression: str | None = None

    name: str | None = None
