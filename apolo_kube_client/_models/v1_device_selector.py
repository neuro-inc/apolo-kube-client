from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_cel_device_selector import V1CELDeviceSelector
from pydantic import BeforeValidator

__all__ = ("V1DeviceSelector",)


class V1DeviceSelector(BaseModel):
    """DeviceSelector must have exactly one field set."""

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.DeviceSelector"

    cel: Annotated[
        V1CELDeviceSelector | None,
        Field(
            description="""CEL contains a CEL expression for selecting a device.""",
            exclude_if=lambda v: v is None,
        ),
        BeforeValidator(_default_if_none(V1CELDeviceSelector)),
    ] = None
