from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_mutating_admission_policy_spec import V1alpha1MutatingAdmissionPolicySpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1MutatingAdmissionPolicy",)


class V1alpha1MutatingAdmissionPolicy(ResourceModel):
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
        V1alpha1MutatingAdmissionPolicySpec,
        BeforeValidator(_default_if_none(V1alpha1MutatingAdmissionPolicySpec)),
    ] = Field(default_factory=lambda: V1alpha1MutatingAdmissionPolicySpec())
