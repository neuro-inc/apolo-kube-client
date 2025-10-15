from pydantic import BaseModel, Field

from .v1_toleration import V1Toleration


class V1Scheduling(BaseModel):
    node_selector: dict(str, str) | None = Field(None, alias="nodeSelector")

    tolerations: list[V1Toleration] | None = Field(None, alias="tolerations")
