from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1beta1_validating_admission_policy_binding import (
    V1beta1ValidatingAdmissionPolicyBinding,
)


class V1beta1ValidatingAdmissionPolicyBindingList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1beta1ValidatingAdmissionPolicyBinding] | None = Field(
        None, alias="items"
    )

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
