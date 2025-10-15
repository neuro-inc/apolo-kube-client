from pydantic import BaseModel, Field

from .v1_resource_claim import V1ResourceClaim


class V1ResourceRequirements(BaseModel):
    claims: list[V1ResourceClaim] | None = Field(None, alias="claims")

    limits: dict(str, str) | None = Field(None, alias="limits")

    requests: dict(str, str) | None = Field(None, alias="requests")
