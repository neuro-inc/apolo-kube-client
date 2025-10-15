from pydantic import BaseModel, Field

from .v1_condition import V1Condition
from .v1beta1_type_checking import V1beta1TypeChecking


class V1beta1ValidatingAdmissionPolicyStatus(BaseModel):
    conditions: list[V1Condition] | None = Field(None, alias="conditions")

    observed_generation: int | None = Field(None, alias="observedGeneration")

    type_checking: V1beta1TypeChecking | None = Field(None, alias="typeChecking")
