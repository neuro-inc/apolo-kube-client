from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1alpha1_mutating_admission_policy_binding_spec import (
    V1alpha1MutatingAdmissionPolicyBindingSpec,
)


class V1alpha1MutatingAdmissionPolicyBinding(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1alpha1MutatingAdmissionPolicyBindingSpec | None = Field(None, alias="spec")
