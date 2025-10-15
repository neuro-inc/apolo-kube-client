from pydantic import BaseModel, Field


class V1GRPCAction(BaseModel):
    port: int | None = Field(None, alias="port")

    service: str | None = Field(None, alias="service")
