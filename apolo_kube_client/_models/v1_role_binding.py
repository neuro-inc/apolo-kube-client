from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .rbac_v1_subject import RbacV1Subject
from .v1_object_meta import V1ObjectMeta
from .v1_role_ref import V1RoleRef
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1RoleBinding",)


class V1RoleBinding(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    role_ref: Annotated[V1RoleRef, BeforeValidator(_default_if_none(V1RoleRef))] = (
        Field(
            default_factory=lambda: V1RoleRef(),
            serialization_alias="roleRef",
            validation_alias=AliasChoices("role_ref", "roleRef"),
        )
    )

    subjects: list[RbacV1Subject] = []
