from pydantic import BaseModel


__all__ = ("V1alpha1JSONPatch",)


class V1alpha1JSONPatch(BaseModel):
    expression: str | None = None
