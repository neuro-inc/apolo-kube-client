from pydantic import BaseModel


__all__ = ("V1ForNode",)


class V1ForNode(BaseModel):
    name: str | None = None
