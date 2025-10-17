from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_condition import V1Condition
from .v1_type_checking import V1TypeChecking

__all__ = ("V1ValidatingAdmissionPolicyStatus",)


class V1ValidatingAdmissionPolicyStatus(BaseModel):
    conditions: list[V1Condition] = Field(default_factory=lambda: [])

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )

    type_checking: V1TypeChecking = Field(
        default_factory=lambda: V1TypeChecking(), alias="typeChecking"
    )
