from pydantic import AliasChoices, BaseModel, Field
from .rbac_v1_subject import RbacV1Subject
from .v1_object_meta import V1ObjectMeta
from .v1_role_ref import V1RoleRef

__all__ = ("V1ClusterRoleBinding",)


class V1ClusterRoleBinding(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    role_ref: V1RoleRef = Field(
        default_factory=lambda: V1RoleRef(),
        serialization_alias="roleRef",
        validation_alias=AliasChoices("role_ref", "roleRef"),
    )

    subjects: list[RbacV1Subject] = []
