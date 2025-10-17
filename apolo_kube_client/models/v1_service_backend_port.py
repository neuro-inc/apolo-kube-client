from pydantic import BaseModel


__all__ = ("V1ServiceBackendPort",)


class V1ServiceBackendPort(BaseModel):
    name: str | None = None

    number: int | None = None
