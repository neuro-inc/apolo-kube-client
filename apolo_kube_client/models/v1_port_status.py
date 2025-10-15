from pydantic import BaseModel, Field


class V1PortStatus(BaseModel):
    error: str | None = Field(None, alias="error")

    port: int | None = Field(None, alias="port")

    protocol: str | None = Field(None, alias="protocol")
