from pydantic import BaseModel


__all__ = ("V1HostIP",)


class V1HostIP(BaseModel):
    ip: str | None = None
