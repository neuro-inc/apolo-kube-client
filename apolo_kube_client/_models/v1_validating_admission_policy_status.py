from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_condition import V1Condition
from .v1_type_checking import V1TypeChecking
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingAdmissionPolicyStatus",)


class V1ValidatingAdmissionPolicyStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = []

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )

    type_checking: Annotated[
        V1TypeChecking, BeforeValidator(_default_if_none(V1TypeChecking))
    ] = Field(
        default_factory=lambda: V1TypeChecking(),
        serialization_alias="typeChecking",
        validation_alias=AliasChoices("type_checking", "typeChecking"),
    )
