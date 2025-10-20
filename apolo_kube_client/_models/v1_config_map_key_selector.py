from pydantic import BaseModel


__all__ = ("V1ConfigMapKeySelector",)


class V1ConfigMapKeySelector(BaseModel):
    key: str | None = None

    name: str | None = None

    optional: bool | None = None
