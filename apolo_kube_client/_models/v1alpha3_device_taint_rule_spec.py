from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1alpha3_device_taint import V1alpha3DeviceTaint
from .v1alpha3_device_taint_selector import V1alpha3DeviceTaintSelector
from pydantic import BeforeValidator

__all__ = ("V1alpha3DeviceTaintRuleSpec",)


class V1alpha3DeviceTaintRuleSpec(BaseModel):
    """DeviceTaintRuleSpec specifies the selector and one taint."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1alpha3.DeviceTaintRuleSpec"
    )

    device_selector: Annotated[
        V1alpha3DeviceTaintSelector,
        Field(
            alias="deviceSelector",
            description="""DeviceSelector defines which device(s) the taint is applied to. All selector criteria must be satified for a device to match. The empty selector matches all devices. Without a selector, no devices are matches.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1alpha3DeviceTaintSelector)),
    ] = V1alpha3DeviceTaintSelector()

    taint: Annotated[
        V1alpha3DeviceTaint,
        Field(description="""The taint that gets applied to matching devices."""),
    ]
