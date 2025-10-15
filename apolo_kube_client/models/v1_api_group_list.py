from pydantic import BaseModel, Field

from .v1_a_p_i_group import V1APIGroup


class V1APIGroupList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    groups: list[V1APIGroup] | None = Field(None, alias="groups")

    kind: str | None = Field(None, alias="kind")
