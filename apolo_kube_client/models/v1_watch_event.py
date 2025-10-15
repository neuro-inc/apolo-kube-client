from pydantic import BaseModel, Field

from .object import object


class V1WatchEvent(BaseModel):
    object: object | None = Field(None, alias="object")

    type: str | None = Field(None, alias="type")
