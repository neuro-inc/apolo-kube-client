from pydantic import BaseModel, Field


class V1ResourceFieldSelector(BaseModel):
    container_name: str | None = Field(None, alias="containerName")

    divisor: str | None = Field(None, alias="divisor")

    resource: str | None = Field(None, alias="resource")
