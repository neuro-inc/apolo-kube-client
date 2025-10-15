from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector


class V2MetricIdentifier(BaseModel):
    name: str | None = Field(None, alias="name")

    selector: V1LabelSelector | None = Field(None, alias="selector")
