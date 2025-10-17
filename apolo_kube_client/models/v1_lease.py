from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_lease_spec import V1LeaseSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Lease",)


class V1Lease(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1LeaseSpec = Field(default_factory=lambda: V1LeaseSpec())
