from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1ScopedResourceSelectorRequirement",)


class V1ScopedResourceSelectorRequirement(BaseModel):
    """A scoped-resource selector requirement is a selector that contains values, a scope name, and an operator that relates the scope name and values."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ScopedResourceSelectorRequirement"
    )

    operator: Annotated[
        str,
        Field(
            description="""Represents a scope's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist."""
        ),
    ]

    scope_name: Annotated[
        str,
        Field(
            alias="scopeName",
            description="""The name of the scope that the selector applies to.""",
        ),
    ]

    values: Annotated[
        list[str],
        Field(
            description="""An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
