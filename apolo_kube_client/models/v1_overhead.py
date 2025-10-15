from pydantic import BaseModel, Field


class V1Overhead(BaseModel):
    pod_fixed: dict(str, str) | None = Field(None, alias="podFixed")
