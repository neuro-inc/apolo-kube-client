from pydantic import AliasChoices, Field
from .base import ListModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1alpha1_mutating_admission_policy import V1alpha1MutatingAdmissionPolicy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1MutatingAdmissionPolicyList",)


class V1alpha1MutatingAdmissionPolicyList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: Annotated[
        list[V1alpha1MutatingAdmissionPolicy],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
