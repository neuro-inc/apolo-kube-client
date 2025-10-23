from pydantic import AliasChoices, Field
from .base import ResourceModel
from .rbac_v1_subject import RbacV1Subject
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_role_ref import V1RoleRef
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ClusterRoleBinding",)


class V1ClusterRoleBinding(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    role_ref: Annotated[V1RoleRef, BeforeValidator(_default_if_none(V1RoleRef))] = (
        Field(
            default_factory=lambda: V1RoleRef(),
            serialization_alias="roleRef",
            validation_alias=AliasChoices("role_ref", "roleRef"),
            exclude_if=_exclude_if,
        )
    )

    subjects: Annotated[
        list[RbacV1Subject], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
