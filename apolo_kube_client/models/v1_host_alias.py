from pydantic import BaseModel


__all__ = ("V1HostAlias",)


class V1HostAlias(BaseModel):
    hostnames: list[str] = []

    ip: str | None = None
