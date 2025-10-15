from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha1_mutating_admission_policy_binding import (
    V1alpha1MutatingAdmissionPolicyBinding,
)


class V1alpha1MutatingAdmissionPolicyBindingList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha1MutatingAdmissionPolicyBinding] | None = Field(
        None, alias="items"
    )

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
