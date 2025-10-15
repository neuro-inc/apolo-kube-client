from pydantic import BaseModel, Field


class V1ImageVolumeSource(BaseModel):
    pull_policy: str | None = Field(None, alias="pullPolicy")

    reference: str | None = Field(None, alias="reference")
