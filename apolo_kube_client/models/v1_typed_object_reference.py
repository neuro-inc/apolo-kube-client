from pydantic import BaseModel, Field


class V1TypedObjectReference(BaseModel):
    api_group: str | None = Field(None, alias="apiGroup")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")
