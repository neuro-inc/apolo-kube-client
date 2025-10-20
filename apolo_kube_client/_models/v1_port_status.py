from pydantic import BaseModel


__all__ = ("V1PortStatus",)


class V1PortStatus(BaseModel):
    error: str | None = None

    port: int | None = None

    protocol: str | None = None
