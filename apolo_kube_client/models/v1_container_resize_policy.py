from pydantic import BaseModel, Field


class V1ContainerResizePolicy(BaseModel):
    resource_name: str | None = Field(None, alias="resourceName")

    restart_policy: str | None = Field(None, alias="restartPolicy")
