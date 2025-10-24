from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1Condition",)


class V1Condition(BaseModel):
    """Condition contains details for one aspect of the current state of this API Resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.Condition"
    )

    last_transition_time: Annotated[
        datetime,
        Field(
            alias="lastTransitionTime",
            description="""lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.""",
        ),
    ]

    message: Annotated[
        str,
        Field(
            description="""message is a human readable message indicating details about the transition. This may be an empty string."""
        ),
    ]

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str,
        Field(
            description="""reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty."""
        ),
    ]

    status: Annotated[
        str,
        Field(description="""status of the condition, one of True, False, Unknown."""),
    ]

    type: Annotated[
        str,
        Field(
            description="""type of condition in CamelCase or in foo.example.com/CamelCase."""
        ),
    ]
