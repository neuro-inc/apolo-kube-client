from pydantic import BaseModel, Field


class V1beta1DeviceConstraint(BaseModel):
    match_attribute: str | None = Field(None, alias="matchAttribute")

    requests: list[str] | None = Field(None, alias="requests")
