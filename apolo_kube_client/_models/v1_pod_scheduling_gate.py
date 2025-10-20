from pydantic import BaseModel


__all__ = ("V1PodSchedulingGate",)


class V1PodSchedulingGate(BaseModel):
    name: str | None = None
