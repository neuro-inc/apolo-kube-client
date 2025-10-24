from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_flow_schema_condition import V1FlowSchemaCondition
from pydantic import BeforeValidator

__all__ = ("V1FlowSchemaStatus",)


class V1FlowSchemaStatus(BaseModel):
    """FlowSchemaStatus represents the current state of a FlowSchema."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.flowcontrol.v1.FlowSchemaStatus"

    conditions: Annotated[
        list[V1FlowSchemaCondition],
        Field(
            description="""`conditions` is a list of the current states of FlowSchema.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
