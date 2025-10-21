from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1beta1_lease_candidate_spec import V1beta1LeaseCandidateSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1LeaseCandidate",)


class V1beta1LeaseCandidate(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1beta1LeaseCandidateSpec,
        BeforeValidator(_default_if_none(V1beta1LeaseCandidateSpec)),
    ] = Field(default_factory=lambda: V1beta1LeaseCandidateSpec())
