from pydantic import BaseModel


__all__ = ("V1HostPathVolumeSource",)


class V1HostPathVolumeSource(BaseModel):
    path: str | None = None

    type: str | None = None
