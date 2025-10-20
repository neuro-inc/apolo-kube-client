from pydantic import BaseModel


__all__ = ("V1beta1Counter",)


class V1beta1Counter(BaseModel):
    value: str | None = None
