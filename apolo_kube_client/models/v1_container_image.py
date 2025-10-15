from pydantic import BaseModel, Field


class V1ContainerImage(BaseModel):
    names: list[str] | None = Field(None, alias="names")

    size_bytes: int | None = Field(None, alias="sizeBytes")
