from pydantic import BaseModel


__all__ = ("V1beta1ApplyConfiguration",)


class V1beta1ApplyConfiguration(BaseModel):
    expression: str | None = None
