from pydantic import BaseModel


__all__ = ("V1ContainerStateWaiting",)


class V1ContainerStateWaiting(BaseModel):
    message: str | None = None

    reason: str | None = None
