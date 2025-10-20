from pydantic import BaseModel


__all__ = ("V1alpha1Variable",)


class V1alpha1Variable(BaseModel):
    expression: str | None = None

    name: str | None = None
