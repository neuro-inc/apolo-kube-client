from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1beta1_validating_admission_policy_spec import (
    V1beta1ValidatingAdmissionPolicySpec,
)
from .v1beta1_validating_admission_policy_status import (
    V1beta1ValidatingAdmissionPolicyStatus,
)


class V1beta1ValidatingAdmissionPolicy(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1beta1ValidatingAdmissionPolicySpec | None = Field(None, alias="spec")

    status: V1beta1ValidatingAdmissionPolicyStatus | None = Field(None, alias="status")
