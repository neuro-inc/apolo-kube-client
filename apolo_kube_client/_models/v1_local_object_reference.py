from pydantic import BaseModel


__all__ = ("V1LocalObjectReference",)


class V1LocalObjectReference(BaseModel):
    name: str | None = None
