from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_limit_range_item import V1LimitRangeItem

__all__ = ("V1LimitRangeSpec",)


class V1LimitRangeSpec(BaseModel):
    """LimitRangeSpec defines a min/max usage limit for resources that match on kind."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.LimitRangeSpec"

    limits: Annotated[
        list[V1LimitRangeItem],
        Field(
            description="""Limits is the list of LimitRangeItem objects that are enforced."""
        ),
    ]
