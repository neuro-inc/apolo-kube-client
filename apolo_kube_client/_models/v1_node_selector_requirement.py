from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1NodeSelectorRequirement",)


class V1NodeSelectorRequirement(BaseModel):
    """A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeSelectorRequirement"

    key: Annotated[
        str, Field(description="""The label key that the selector applies to.""")
    ]

    operator: Annotated[
        str,
        Field(
            description="""Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt."""
        ),
    ]

    values: Annotated[
        list[str],
        Field(
            description="""An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
