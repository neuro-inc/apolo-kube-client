from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_counter import V1Counter

__all__ = ("V1DeviceCounterConsumption",)


class V1DeviceCounterConsumption(BaseModel):
    """DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1.DeviceCounterConsumption"
    )

    counter_set: Annotated[
        str,
        Field(
            alias="counterSet",
            description="""CounterSet is the name of the set from which the counters defined will be consumed.""",
        ),
    ]

    counters: Annotated[
        dict[str, V1Counter],
        Field(
            description="""Counters defines the counters that will be consumed by the device.

The maximum number counters in a device is 32. In addition, the maximum number of all counters in all devices is 1024 (for example, 64 devices with 16 counters each)."""
        ),
    ]
