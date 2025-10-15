from pydantic import BaseModel, Field


class V1OwnerReference(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    block_owner_deletion: bool | None = Field(None, alias="blockOwnerDeletion")

    controller: bool | None = Field(None, alias="controller")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    uid: str | None = Field(None, alias="uid")
