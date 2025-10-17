from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_condition import V1Condition
from .v1_type_checking import V1TypeChecking

__all__ = ("V1ValidatingAdmissionPolicyStatus",)


class V1ValidatingAdmissionPolicyStatus(BaseModel):
    conditions: list[V1Condition] = Field(default=[])

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )

    type_checking: V1TypeChecking = Field(
        default_factory=lambda: V1TypeChecking(),
        serialization_alias="typeChecking",
        validation_alias=AliasChoices("type_checking", "typeChecking"),
    )
