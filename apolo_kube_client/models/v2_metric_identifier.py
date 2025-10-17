from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V2MetricIdentifier",)


class V2MetricIdentifier(BaseModel):
    name: str | None = Field(default=None)

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())
