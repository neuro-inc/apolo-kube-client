from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1LabelSelectorRequirement",)


class V1LabelSelectorRequirement(BaseModel):
    """A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement"
    )

    key: Annotated[
        str, Field(description="""key is the label key that the selector applies to.""")
    ]

    operator: Annotated[
        str,
        Field(
            description="""operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist."""
        ),
    ]

    values: Annotated[
        list[str],
        Field(
            description="""values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
