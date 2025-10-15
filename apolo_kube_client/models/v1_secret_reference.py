from pydantic import BaseModel, Field


class V1SecretReference(BaseModel):
    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")
