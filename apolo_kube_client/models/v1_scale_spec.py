from pydantic import BaseModel


__all__ = ("V1ScaleSpec",)


class V1ScaleSpec(BaseModel):
    replicas: int | None = None
