from pydantic import BaseModel, Field

from .rbac_v1_subject import RbacV1Subject
from .v1_object_meta import V1ObjectMeta
from .v1_role_ref import V1RoleRef


class V1ClusterRoleBinding(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    role_ref: V1RoleRef | None = Field(None, alias="roleRef")

    subjects: list[RbacV1Subject] | None = Field(None, alias="subjects")
