from pydantic import BaseModel


__all__ = ("V1ScaleStatus",)


class V1ScaleStatus(BaseModel):
    replicas: int | None = None

    selector: str | None = None
