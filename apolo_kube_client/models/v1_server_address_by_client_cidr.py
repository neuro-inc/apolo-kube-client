from pydantic import BaseModel, Field


class V1ServerAddressByClientCIDR(BaseModel):
    client_cidr: str | None = Field(None, alias="clientCIDR")

    server_address: str | None = Field(None, alias="serverAddress")
