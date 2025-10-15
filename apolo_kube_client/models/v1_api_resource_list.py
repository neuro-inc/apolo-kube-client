from pydantic import BaseModel, Field

from .v1_a_p_i_resource import V1APIResource


class V1APIResourceList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    group_version: str | None = Field(None, alias="groupVersion")

    kind: str | None = Field(None, alias="kind")

    resources: list[V1APIResource] | None = Field(None, alias="resources")
