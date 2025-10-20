from pydantic import BaseModel


__all__ = ("V1VolumeNodeResources",)


class V1VolumeNodeResources(BaseModel):
    count: int | None = None
