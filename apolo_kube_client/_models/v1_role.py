from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base import ResourceModel
from .utils import KubeMeta, _collection_if_none, _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_policy_rule import V1PolicyRule


__all__ = ("V1Role",)


class V1Role(ResourceModel):
    """Role is a namespaced, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.rbac.v1.Role"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="rbac.authorization.k8s.io", kind="Role", version="v1"
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
    ] = "Role"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    rules: Annotated[
        list[V1PolicyRule],
        Field(
            description="""Rules holds all the PolicyRules for this Role""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
