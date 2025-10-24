from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1alpha1StorageVersionCondition",)


class V1alpha1StorageVersionCondition(BaseModel):
    """Describes the state of the storageVersion at a certain point."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.apiserverinternal.v1alpha1.StorageVersionCondition"
    )

    last_transition_time: Annotated[
        datetime | None,
        Field(
            alias="lastTransitionTime",
            description="""Last time the condition transitioned from one status to another.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str,
        Field(
            description="""A human readable message indicating details about the transition."""
        ),
    ]

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""If set, this represents the .metadata.generation that the condition was set based upon.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str, Field(description="""The reason for the condition's last transition.""")
    ]

    status: Annotated[
        str,
        Field(description="""Status of the condition, one of True, False, Unknown."""),
    ]

    type: Annotated[str, Field(description="""Type of the condition.""")]
