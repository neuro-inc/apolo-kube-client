from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_validating_admission_policy_spec import V1ValidatingAdmissionPolicySpec
from .v1_validating_admission_policy_status import V1ValidatingAdmissionPolicyStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingAdmissionPolicy",)


class V1ValidatingAdmissionPolicy(ResourceModel):
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
        V1ValidatingAdmissionPolicySpec,
        BeforeValidator(_default_if_none(V1ValidatingAdmissionPolicySpec)),
    ] = Field(default_factory=lambda: V1ValidatingAdmissionPolicySpec())

    status: Annotated[
        V1ValidatingAdmissionPolicyStatus,
        BeforeValidator(_default_if_none(V1ValidatingAdmissionPolicyStatus)),
    ] = Field(default_factory=lambda: V1ValidatingAdmissionPolicyStatus())
