from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1beta1ParamRef",)


class V1beta1ParamRef(BaseModel):
    name: str | None = Field(default_factory=lambda: None)

    namespace: str | None = Field(default_factory=lambda: None)

    parameter_not_found_action: str | None = Field(
        default_factory=lambda: None, alias="parameterNotFoundAction"
    )

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())
