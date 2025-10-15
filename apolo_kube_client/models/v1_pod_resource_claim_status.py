from pydantic import BaseModel, Field


class V1PodResourceClaimStatus(BaseModel):
    name: str | None = Field(None, alias="name")

    resource_claim_name: str | None = Field(None, alias="resourceClaimName")
