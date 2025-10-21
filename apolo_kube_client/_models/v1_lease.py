from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_lease_spec import V1LeaseSpec
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Lease",)


class V1Lease(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[V1LeaseSpec, BeforeValidator(_default_if_none(V1LeaseSpec))] = (
        Field(default_factory=lambda: V1LeaseSpec())
    )
