from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1beta2_counter import V1beta2Counter


__all__ = ("V1beta2DeviceCounterConsumption",)


class V1beta2DeviceCounterConsumption(BaseConfiguredModel):
    """DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta2.DeviceCounterConsumption"
    )

    counter_set: Annotated[
        str,
        Field(
            alias="counterSet",
            description="""CounterSet is the name of the set from which the counters defined will be consumed.""",
        ),
    ]

    counters: Annotated[
        dict[str, V1beta2Counter],
        Field(
            description="""Counters defines the counters that will be consumed by the device.

The maximum number counters in a device is 32. In addition, the maximum number of all counters in all devices is 1024 (for example, 64 devices with 16 counters each)."""
        ),
    ]
