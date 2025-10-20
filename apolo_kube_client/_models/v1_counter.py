from pydantic import BaseModel


__all__ = ("V1Counter",)


class V1Counter(BaseModel):
    value: str | None = None
