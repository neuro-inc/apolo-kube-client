from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1alpha1ParamRef",)


class V1alpha1ParamRef(BaseModel):
    name: str | None = Field(default_factory=lambda: None, alias="name")

    namespace: str | None = Field(default_factory=lambda: None, alias="namespace")

    parameter_not_found_action: str | None = Field(
        default_factory=lambda: None, alias="parameterNotFoundAction"
    )

    selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="selector"
    )
