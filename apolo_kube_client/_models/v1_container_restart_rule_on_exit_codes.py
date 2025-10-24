from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1ContainerRestartRuleOnExitCodes",)


class V1ContainerRestartRuleOnExitCodes(BaseModel):
    """ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ContainerRestartRuleOnExitCodes"
    )

    operator: Annotated[
        str,
        Field(
            description="""Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the
  set of specified values.
- NotIn: the requirement is satisfied if the container exit code is
  not in the set of specified values."""
        ),
    ]

    values: Annotated[
        list[int],
        Field(
            description="""Specifies the set of values to check for container exit codes. At most 255 elements are allowed.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
