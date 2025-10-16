from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ServerAddressByClientCIDR",)


class V1ServerAddressByClientCIDR(BaseModel):
    client_cidr: str | None = Field(None, alias="clientCIDR")

    server_address: str | None = Field(None, alias="serverAddress")
