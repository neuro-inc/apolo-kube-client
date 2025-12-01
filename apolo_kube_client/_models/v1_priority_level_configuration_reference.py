from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1PriorityLevelConfigurationReference",)


class V1PriorityLevelConfigurationReference(BaseModel):
    """PriorityLevelConfigurationReference contains information that points to the "request-priority" being used."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationReference"
    )

    name: Annotated[
        str,
        Field(
            description="""`name` is the name of the priority level configuration being referenced Required."""
        ),
    ]
