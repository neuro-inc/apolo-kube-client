from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ContainerResizePolicy",)


class V1ContainerResizePolicy(BaseModel):
    resource_name: str | None = Field(None, alias="resourceName")

    restart_policy: str | None = Field(None, alias="restartPolicy")
