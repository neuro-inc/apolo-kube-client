from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1PersistentVolumeStatus",)


class V1PersistentVolumeStatus(BaseModel):
    """PersistentVolumeStatus is the current status of a persistent volume."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PersistentVolumeStatus"

    last_phase_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastPhaseTransitionTime",
            description="""lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""message is a human-readable message indicating details about why the volume is in this state.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    phase: Annotated[
        str | None,
        Field(
            description="""phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
