from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_access_review_spec import V1SelfSubjectAccessReviewSpec
from .v1_subject_access_review_status import V1SubjectAccessReviewStatus
from pydantic import BeforeValidator

__all__ = ("V1SelfSubjectAccessReview",)


class V1SelfSubjectAccessReview(ResourceModel):
    """SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a spec.namespace means "in all namespaces".  Self is a special case, because users should always be able to check whether they can perform an action"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.SelfSubjectAccessReview"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="authorization.k8s.io", kind="SelfSubjectAccessReview", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "authorization.k8s.io/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "SelfSubjectAccessReview"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1SelfSubjectAccessReviewSpec,
        Field(
            description="""Spec holds information about the request being evaluated.  user and groups must be empty"""
        ),
    ]

    status: Annotated[
        V1SubjectAccessReviewStatus | None,
        Field(
            description="""Status is filled in by the server and indicates whether the request is allowed or not""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
