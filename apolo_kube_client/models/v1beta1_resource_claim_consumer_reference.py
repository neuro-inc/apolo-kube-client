from pydantic import BaseModel, Field


class V1beta1ResourceClaimConsumerReference(BaseModel):
    api_group: str | None = Field(None, alias="apiGroup")

    name: str | None = Field(None, alias="name")

    resource: str | None = Field(None, alias="resource")

    uid: str | None = Field(None, alias="uid")
