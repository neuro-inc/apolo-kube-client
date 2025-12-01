from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _default_if_none
from .v1beta1_basic_device import V1beta1BasicDevice


__all__ = ("V1beta1Device",)


class V1beta1Device(BaseConfiguredModel):
    """Device represents one individual hardware instance that can be selected based on its attributes. Besides the name, exactly one field must be set."""

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
