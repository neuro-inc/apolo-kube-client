from pydantic import BaseModel


__all__ = ("V1ForZone",)


class V1ForZone(BaseModel):
    name: str | None = None
