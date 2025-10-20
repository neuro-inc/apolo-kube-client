from pydantic import BaseModel


__all__ = ("V1IngressPortStatus",)


class V1IngressPortStatus(BaseModel):
    error: str | None = None

    port: int | None = None

    protocol: str | None = None
