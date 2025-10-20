from pydantic import BaseModel


__all__ = ("V1beta1Variable",)


class V1beta1Variable(BaseModel):
    expression: str | None = None

    name: str | None = None
