from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1alpha3DeviceTaint",)


class V1alpha3DeviceTaint(BaseModel):
    """The device this taint is attached to has the "effect" on any claim which does not tolerate the taint and, through the claim, to pods using the claim."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1alpha3.DeviceTaint"

    effect: Annotated[
        str,
        Field(
            description="""The effect of the taint on claims that do not tolerate the taint and through such claims on the pods using them. Valid effects are NoSchedule and NoExecute. PreferNoSchedule as used for nodes is not valid here."""
        ),
    ]

    key: Annotated[
        str,
        Field(
            description="""The taint key to be applied to a device. Must be a label name."""
        ),
    ]

    time_added: Annotated[
        datetime | None,
        Field(
            alias="timeAdded",
            description="""TimeAdded represents the time at which the taint was added. Added automatically during create or update if not set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    value: Annotated[
        str | None,
        Field(
            description="""The taint value corresponding to the taint key. Must be a label value.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
