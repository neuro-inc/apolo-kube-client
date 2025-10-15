from pydantic import BaseModel, Field


class V1ExternalDocumentation(BaseModel):
    description: str | None = Field(None, alias="description")

    url: str | None = Field(None, alias="url")
