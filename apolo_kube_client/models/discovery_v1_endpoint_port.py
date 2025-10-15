from pydantic import BaseModel, Field


class DiscoveryV1EndpointPort(BaseModel):
    app_protocol: str | None = Field(None, alias="appProtocol")

    name: str | None = Field(None, alias="name")

    port: int | None = Field(None, alias="port")

    protocol: str | None = Field(None, alias="protocol")
