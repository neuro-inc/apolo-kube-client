from pydantic import BaseModel, Field


class V1ScaleSpec(BaseModel):
    replicas: int | None = Field(None, alias="replicas")
