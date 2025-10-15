from pydantic import BaseModel, Field


class V1DaemonEndpoint(BaseModel):
    port: int | None = Field(None, alias="Port")
