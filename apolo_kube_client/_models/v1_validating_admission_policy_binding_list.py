from pydantic import AliasChoices, Field
from .base import ListModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_list_meta import V1ListMeta
from .v1_validating_admission_policy_binding import V1ValidatingAdmissionPolicyBinding
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingAdmissionPolicyBindingList",)


class V1ValidatingAdmissionPolicyBindingList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    items: Annotated[
        list[V1ValidatingAdmissionPolicyBinding],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta(), exclude_if=_exclude_if)
    )
