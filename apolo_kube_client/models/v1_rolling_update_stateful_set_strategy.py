from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

__all__ = ("V1RollingUpdateStatefulSetStrategy",)


class V1RollingUpdateStatefulSetStrategy(BaseModel):
    max_unavailable: JsonType | None = Field(None, alias="maxUnavailable")

    partition: int | None = Field(None, alias="partition")
