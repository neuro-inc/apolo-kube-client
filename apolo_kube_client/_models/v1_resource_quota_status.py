from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1ResourceQuotaStatus",)


class V1ResourceQuotaStatus(BaseModel):
    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

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
