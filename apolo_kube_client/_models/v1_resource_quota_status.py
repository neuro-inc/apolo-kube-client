from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none


__all__ = ("V1ResourceQuotaStatus",)


class V1ResourceQuotaStatus(BaseConfiguredModel):
    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ResourceQuotaStatus"

    hard: Annotated[
        dict[str, str],
        Field(
            description="""Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    used: Annotated[
        dict[str, str],
        Field(
            description="""Used is the current observed total usage of the resource in the namespace.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}
