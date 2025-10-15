from pydantic import BaseModel, Field


class V1HostAlias(BaseModel):
    hostnames: list[str] | None = Field(None, alias="hostnames")

    ip: str | None = Field(None, alias="ip")
