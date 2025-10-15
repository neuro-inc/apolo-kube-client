from pydantic import BaseModel, Field


class V1alpha3DeviceConstraint(BaseModel):
    match_attribute: str | None = Field(None, alias="matchAttribute")

    requests: list[str] | None = Field(None, alias="requests")
