from pydantic import BaseModel


__all__ = ("V1VolumeResourceRequirements",)


class V1VolumeResourceRequirements(BaseModel):
    limits: dict[str, str] = {}

    requests: dict[str, str] = {}
