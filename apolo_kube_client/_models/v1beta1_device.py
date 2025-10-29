from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1beta1_basic_device import V1beta1BasicDevice
from pydantic import BeforeValidator

__all__ = ("V1beta1Device",)


class V1beta1Device(BaseModel):
    """Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta1.Device"

    basic: Annotated[
        V1beta1BasicDevice,
        Field(
            description="""Basic defines one device instance.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1beta1BasicDevice)),
    ] = V1beta1BasicDevice()

    name: Annotated[
        str,
        Field(
            description="""Name is unique identifier among all devices managed by the driver in the pool. It must be a DNS label."""
        ),
    ]
