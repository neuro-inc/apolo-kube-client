from pydantic import BaseModel


__all__ = ("V1beta2Counter",)


class V1beta2Counter(BaseModel):
    value: str | None = None
