from pydantic import BaseModel, Field

from .object import object


class V1RollingUpdateStatefulSetStrategy(BaseModel):
    max_unavailable: object | None = Field(None, alias="maxUnavailable")

    partition: int | None = Field(None, alias="partition")
