from __future__ import annotations
from pydantic import BaseModel, Field
from .rbac_v1_subject import RbacV1Subject
from .v1_object_meta import V1ObjectMeta
from .v1_role_ref import V1RoleRef

__all__ = ("V1RoleBinding",)


class V1RoleBinding(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    role_ref: V1RoleRef = Field(default_factory=lambda: V1RoleRef(), alias="roleRef")

    subjects: list[RbacV1Subject] = Field(default_factory=lambda: [])
