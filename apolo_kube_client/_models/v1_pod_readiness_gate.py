from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PodReadinessGate",)


class V1PodReadinessGate(BaseModel):
    """PodReadinessGate contains the reference to a pod condition"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodReadinessGate"

    condition_type: Annotated[
        str,
        Field(
            alias="conditionType",
            description="""ConditionType refers to a condition in the pod's condition list with matching type.""",
        ),
    ]
