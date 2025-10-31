from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1alpha3_cel_device_selector import V1alpha3CELDeviceSelector

__all__ = ("V1alpha3DeviceSelector",)


class V1alpha3DeviceSelector(BaseModel):
    """DeviceSelector must have exactly one field set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1alpha3.DeviceSelector"

    cel: Annotated[
        V1alpha3CELDeviceSelector | None,
        Field(
            description="""CEL contains a CEL expression for selecting a device.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
