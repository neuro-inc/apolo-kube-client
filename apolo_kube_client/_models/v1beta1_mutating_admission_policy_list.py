from pydantic import AliasChoices, Field
from .base import ListModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_list_meta import V1ListMeta
from .v1beta1_mutating_admission_policy import V1beta1MutatingAdmissionPolicy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1MutatingAdmissionPolicyList",)


class V1beta1MutatingAdmissionPolicyList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    items: Annotated[
        list[V1beta1MutatingAdmissionPolicy], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta(), exclude_if=_exclude_if)
    )
