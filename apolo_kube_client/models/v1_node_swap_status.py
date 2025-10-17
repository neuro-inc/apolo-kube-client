from pydantic import BaseModel


__all__ = ("V1NodeSwapStatus",)


class V1NodeSwapStatus(BaseModel):
    capacity: int | None = None
