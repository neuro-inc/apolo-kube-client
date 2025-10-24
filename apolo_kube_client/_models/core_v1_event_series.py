from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("CoreV1EventSeries",)


class CoreV1EventSeries(BaseModel):
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EventSeries"

    count: Annotated[
        int | None,
        Field(
            description="""Number of occurrences in this series up to the last heartbeat time""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    last_observed_time: Annotated[
        datetime | None,
        Field(
            alias="lastObservedTime",
            description="""Time of the last occurrence observed""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
