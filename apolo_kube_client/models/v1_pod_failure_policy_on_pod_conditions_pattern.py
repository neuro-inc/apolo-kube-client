from pydantic import BaseModel, Field


class V1PodFailurePolicyOnPodConditionsPattern(BaseModel):
    status: str | None = Field(None, alias="status")

    type: str | None = Field(None, alias="type")
