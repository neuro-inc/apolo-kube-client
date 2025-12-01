from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1PriorityLevelConfigurationReference",)


class V1PriorityLevelConfigurationReference(BaseConfiguredModel):
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
