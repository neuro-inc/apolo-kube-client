from pydantic import BaseModel, Field

from .v1_resource_health import V1ResourceHealth


class V1ResourceStatus(BaseModel):
    name: str | None = Field(None, alias="name")

    resources: list[V1ResourceHealth] | None = Field(None, alias="resources")
