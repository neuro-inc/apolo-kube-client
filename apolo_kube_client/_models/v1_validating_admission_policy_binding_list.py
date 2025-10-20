from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1_validating_admission_policy_binding import V1ValidatingAdmissionPolicyBinding

__all__ = ("V1ValidatingAdmissionPolicyBindingList",)


class V1ValidatingAdmissionPolicyBindingList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ValidatingAdmissionPolicyBinding] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
