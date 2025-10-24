from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1Taint",)


class V1Taint(BaseModel):
    """The node this Taint is attached to has the "effect" on any pod that does not tolerate the Taint."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Taint"

    effect: Annotated[
        str,
        Field(
            description="""Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute."""
        ),
    ]

    key: Annotated[
        str, Field(description="""Required. The taint key to be applied to a node.""")
    ]

    time_added: Annotated[
        datetime | None,
        Field(
            alias="timeAdded",
            description="""TimeAdded represents the time at which the taint was added.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    value: Annotated[
        str | None,
        Field(
            description="""The taint value corresponding to the taint key.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
