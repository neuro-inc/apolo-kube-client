from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2MetricIdentifier",)


class V2MetricIdentifier(BaseModel):
    name: str | None = None

    selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(default_factory=lambda: V1LabelSelector())
