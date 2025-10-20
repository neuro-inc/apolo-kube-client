from pydantic import BaseModel


__all__ = ("V1alpha1ApplyConfiguration",)


class V1alpha1ApplyConfiguration(BaseModel):
    expression: str | None = None
