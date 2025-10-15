from pydantic import BaseModel, Field

from .object import object


class V1TCPSocketAction(BaseModel):
    host: str | None = Field(None, alias="host")

    port: object | None = Field(None, alias="port")
