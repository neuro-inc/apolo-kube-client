from pydantic import BaseModel
from .v1_resource_health import V1ResourceHealth

__all__ = ("V1ResourceStatus",)


class V1ResourceStatus(BaseModel):
    name: str | None = None

    resources: list[V1ResourceHealth] = []
