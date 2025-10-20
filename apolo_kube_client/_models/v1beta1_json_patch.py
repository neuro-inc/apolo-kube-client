from pydantic import BaseModel


__all__ = ("V1beta1JSONPatch",)


class V1beta1JSONPatch(BaseModel):
    expression: str | None = None
