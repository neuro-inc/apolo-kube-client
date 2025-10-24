from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1LimitRangeItem",)


class V1LimitRangeItem(BaseModel):
    """LimitRangeItem defines a min/max usage limit for any resource that matches on kind."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.LimitRangeItem"

    default: Annotated[
        dict[str, str],
        Field(
            description="""Default resource requirement limit value by resource name if resource limit is omitted.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    default_request: Annotated[
        dict[str, str],
        Field(
            alias="defaultRequest",
            description="""DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    max: Annotated[
        dict[str, str],
        Field(
            description="""Max usage constraints on this kind by resource name.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    max_limit_request_ratio: Annotated[
        dict[str, str],
        Field(
            alias="maxLimitRequestRatio",
            description="""MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    min: Annotated[
        dict[str, str],
        Field(
            description="""Min usage constraints on this kind by resource name.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    type: Annotated[
        str, Field(description="""Type of resource that this limit applies to.""")
    ]
