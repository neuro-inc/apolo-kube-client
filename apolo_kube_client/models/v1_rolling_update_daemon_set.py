from pydantic import BaseModel, Field

from .object import object


class V1RollingUpdateDaemonSet(BaseModel):
    max_surge: object | None = Field(None, alias="maxSurge")

    max_unavailable: object | None = Field(None, alias="maxUnavailable")
