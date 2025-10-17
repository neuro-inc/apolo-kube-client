from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha3_device_taint import V1alpha3DeviceTaint
from .v1alpha3_device_taint_selector import V1alpha3DeviceTaintSelector

__all__ = ("V1alpha3DeviceTaintRuleSpec",)


class V1alpha3DeviceTaintRuleSpec(BaseModel):
    device_selector: V1alpha3DeviceTaintSelector = Field(
        default_factory=lambda: V1alpha3DeviceTaintSelector(), alias="deviceSelector"
    )

    taint: V1alpha3DeviceTaint = Field(default_factory=lambda: V1alpha3DeviceTaint())
