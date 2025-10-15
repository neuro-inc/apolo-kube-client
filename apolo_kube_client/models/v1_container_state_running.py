from datetime import datetime

from pydantic import BaseModel, Field


class V1ContainerStateRunning(BaseModel):
    started_at: datetime | None = Field(None, alias="startedAt")
