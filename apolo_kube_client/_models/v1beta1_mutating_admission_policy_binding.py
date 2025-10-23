from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1beta1_mutating_admission_policy_binding_spec import (
    V1beta1MutatingAdmissionPolicyBindingSpec,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1MutatingAdmissionPolicyBinding",)


class V1beta1MutatingAdmissionPolicyBinding(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1beta1MutatingAdmissionPolicyBindingSpec,
        BeforeValidator(_default_if_none(V1beta1MutatingAdmissionPolicyBindingSpec)),
    ] = Field(
        default_factory=lambda: V1beta1MutatingAdmissionPolicyBindingSpec(),
        exclude_if=_exclude_if,
    )
