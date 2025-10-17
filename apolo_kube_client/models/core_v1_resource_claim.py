from pydantic import BaseModel


__all__ = ("CoreV1ResourceClaim",)


class CoreV1ResourceClaim(BaseModel):
    name: str | None = None

    request: str | None = None
