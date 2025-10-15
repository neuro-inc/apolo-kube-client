from pydantic import BaseModel, Field

from .object import object


class V1NetworkPolicyPort(BaseModel):
    end_port: int | None = Field(None, alias="endPort")

    port: object | None = Field(None, alias="port")

    protocol: str | None = Field(None, alias="protocol")
