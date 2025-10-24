from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1beta2_counter import V1beta2Counter

__all__ = ("V1beta2CounterSet",)


class V1beta2CounterSet(BaseModel):
    """CounterSet defines a named set of counters that are available to be used by devices defined in the ResourceSlice.

    The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.CounterSet"

    counters: Annotated[
        dict[str, V1beta2Counter],
        Field(
            description="""Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.

The maximum number of counters in all sets is 32."""
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""Name defines the name of the counter set. It must be a DNS label."""
        ),
    ]
