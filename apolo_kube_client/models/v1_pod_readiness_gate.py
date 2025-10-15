from pydantic import BaseModel, Field


class V1PodReadinessGate(BaseModel):
    condition_type: str | None = Field(None, alias="conditionType")
