from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1alpha3_device_taint import V1alpha3DeviceTaint
from .v1alpha3_device_taint_selector import V1alpha3DeviceTaintSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha3DeviceTaintRuleSpec",)


class V1alpha3DeviceTaintRuleSpec(BaseModel):
    device_selector: Annotated[
        V1alpha3DeviceTaintSelector,
        BeforeValidator(_default_if_none(V1alpha3DeviceTaintSelector)),
    ] = Field(
        default_factory=lambda: V1alpha3DeviceTaintSelector(),
        serialization_alias="deviceSelector",
        validation_alias=AliasChoices("device_selector", "deviceSelector"),
        exclude_if=_exclude_if,
    )

    taint: Annotated[
        V1alpha3DeviceTaint, BeforeValidator(_default_if_none(V1alpha3DeviceTaint))
    ] = Field(default_factory=lambda: V1alpha3DeviceTaint(), exclude_if=_exclude_if)
