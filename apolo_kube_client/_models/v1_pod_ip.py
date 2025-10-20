from pydantic import BaseModel


__all__ = ("V1PodIP",)


class V1PodIP(BaseModel):
    ip: str | None = None
