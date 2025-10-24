from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PriorityLevelConfigurationReference",)


class V1PriorityLevelConfigurationReference(BaseModel):
    """PriorityLevelConfigurationReference contains information that points to the "request-priority" being used."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationReference"
    )

    name: Annotated[
        str,
        Field(
            description="""`name` is the name of the priority level configuration being referenced Required."""
        ),
    ]
