from pydantic import BaseModel, Field

from .object import object


class V1ServicePort(BaseModel):
    app_protocol: str | None = Field(None, alias="appProtocol")

    name: str | None = Field(None, alias="name")

    node_port: int | None = Field(None, alias="nodePort")

    port: int | None = Field(None, alias="port")

    protocol: str | None = Field(None, alias="protocol")

    target_port: object | None = Field(None, alias="targetPort")
