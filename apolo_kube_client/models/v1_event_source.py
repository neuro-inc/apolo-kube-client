from pydantic import BaseModel, Field


class V1EventSource(BaseModel):
    component: str | None = Field(None, alias="component")

    host: str | None = Field(None, alias="host")
