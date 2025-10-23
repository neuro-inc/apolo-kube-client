from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_condition import V1Condition
from .v1_type_checking import V1TypeChecking
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingAdmissionPolicyStatus",)


class V1ValidatingAdmissionPolicyStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
        exclude_if=_exclude_if,
    )

    type_checking: Annotated[
        V1TypeChecking, BeforeValidator(_default_if_none(V1TypeChecking))
    ] = Field(
        default_factory=lambda: V1TypeChecking(),
        serialization_alias="typeChecking",
        validation_alias=AliasChoices("type_checking", "typeChecking"),
        exclude_if=_exclude_if,
    )
