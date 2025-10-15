from pydantic import BaseModel, Field


class V1HostIP(BaseModel):
    ip: str | None = Field(None, alias="ip")
