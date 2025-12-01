from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1PodReadinessGate",)


class V1PodReadinessGate(BaseConfiguredModel):
    """PodReadinessGate contains the reference to a pod condition"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodReadinessGate"

    condition_type: Annotated[
        str,
        Field(
            alias="conditionType",
            description="""ConditionType refers to a condition in the pod's condition list with matching type.""",
        ),
    ]
