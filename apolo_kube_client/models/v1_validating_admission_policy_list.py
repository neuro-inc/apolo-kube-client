from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_validating_admission_policy import V1ValidatingAdmissionPolicy

__all__ = ("V1ValidatingAdmissionPolicyList",)


class V1ValidatingAdmissionPolicyList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ValidatingAdmissionPolicy] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
