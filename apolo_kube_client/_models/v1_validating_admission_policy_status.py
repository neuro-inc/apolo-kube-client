from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_condition import V1Condition
from .v1_type_checking import V1TypeChecking
from pydantic import BeforeValidator

__all__ = ("V1ValidatingAdmissionPolicyStatus",)


class V1ValidatingAdmissionPolicyStatus(BaseModel):
    """ValidatingAdmissionPolicyStatus represents the status of an admission validation policy."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyStatus"
    )

    conditions: Annotated[
        list[V1Condition],
        Field(
            description="""The conditions represent the latest available observations of a policy's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""The generation observed by the controller.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type_checking: Annotated[
        V1TypeChecking,
        Field(
            alias="typeChecking",
            description="""The results of type checking for each expression. Presence of this field indicates the completion of the type checking.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1TypeChecking)),
    ] = V1TypeChecking()
