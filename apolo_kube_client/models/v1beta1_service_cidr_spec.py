from pydantic import BaseModel, Field


class V1beta1ServiceCIDRSpec(BaseModel):
    cidrs: list[str] | None = Field(None, alias="cidrs")
