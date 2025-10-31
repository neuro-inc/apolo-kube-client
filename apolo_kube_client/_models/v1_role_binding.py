from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .rbac_v1_subject import RbacV1Subject
from .utils import KubeMeta
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_role_ref import V1RoleRef
from pydantic import BeforeValidator

__all__ = ("V1RoleBinding",)


class V1RoleBinding(ResourceModel):
    """RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in.  RoleBindings in a given namespace only have effect in that namespace."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.rbac.v1.RoleBinding"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="rbac.authorization.k8s.io", kind="RoleBinding", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "rbac.authorization.k8s.io/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "RoleBinding"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    role_ref: Annotated[
        V1RoleRef,
        Field(
            alias="roleRef",
            description="""RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is immutable.""",
        ),
    ]

    subjects: Annotated[
        list[RbacV1Subject],
        Field(
            description="""Subjects holds references to the objects the role applies to.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
