from pydantic import BaseModel


__all__ = ("V1Sysctl",)


class V1Sysctl(BaseModel):
    name: str | None = None

    value: str | None = None
