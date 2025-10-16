from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

__all__ = ("V1RollingUpdateDeployment",)


class V1RollingUpdateDeployment(BaseModel):
    max_surge: JsonType | None = Field(None, alias="maxSurge")

    max_unavailable: JsonType | None = Field(None, alias="maxUnavailable")
