from pydantic import BaseModel, Field


class V1NodeAddress(BaseModel):
    address: str | None = Field(None, alias="address")

    type: str | None = Field(None, alias="type")
