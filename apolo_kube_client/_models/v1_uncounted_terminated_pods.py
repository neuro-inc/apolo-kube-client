from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1UncountedTerminatedPods",)


class V1UncountedTerminatedPods(BaseModel):
    """UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job status counters."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.UncountedTerminatedPods"

    failed: Annotated[
        list[str],
        Field(
            description="""failed holds UIDs of failed Pods.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    succeeded: Annotated[
        list[str],
        Field(
            description="""succeeded holds UIDs of succeeded Pods.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
