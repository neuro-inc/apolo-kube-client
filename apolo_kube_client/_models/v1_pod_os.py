from pydantic import BaseModel


__all__ = ("V1PodOS",)


class V1PodOS(BaseModel):
    name: str | None = None
