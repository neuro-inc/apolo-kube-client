from pydantic import BaseModel, Field

from .object import object
from .v1_h_t_t_p_header import V1HTTPHeader


class V1HTTPGetAction(BaseModel):
    host: str | None = Field(None, alias="host")

    http_headers: list[V1HTTPHeader] | None = Field(None, alias="httpHeaders")

    path: str | None = Field(None, alias="path")

    port: object | None = Field(None, alias="port")

    scheme: str | None = Field(None, alias="scheme")
