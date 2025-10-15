from pydantic import BaseModel, Field


class V1SecretEnvSource(BaseModel):
    name: str | None = Field(None, alias="name")

    optional: bool | None = Field(None, alias="optional")
