from pydantic import BaseModel, Field


class V1ParamKind(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")
