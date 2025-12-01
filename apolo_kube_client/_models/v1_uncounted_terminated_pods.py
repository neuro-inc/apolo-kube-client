from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none


__all__ = ("V1UncountedTerminatedPods",)


class V1UncountedTerminatedPods(BaseConfiguredModel):
    """UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job status counters."""

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
