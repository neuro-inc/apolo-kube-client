from pydantic import BaseModel, Field


class V1PodIP(BaseModel):
    ip: str | None = Field(None, alias="ip")
