from pydantic import BaseModel, Field


class V1ScaleStatus(BaseModel):
    replicas: int | None = Field(None, alias="replicas")

    selector: str | None = Field(None, alias="selector")
