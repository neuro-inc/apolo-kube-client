from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_subject_access_review_spec import V1SubjectAccessReviewSpec
from .v1_subject_access_review_status import V1SubjectAccessReviewStatus
from pydantic import BeforeValidator

__all__ = ("V1LocalSubjectAccessReview",)


class V1LocalSubjectAccessReview(ResourceModel):
    """LocalSubjectAccessReview checks whether or not a user or group can perform an action in a given namespace. Having a namespace scoped resource makes it much easier to grant namespace scoped policy that includes permissions checking."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.LocalSubjectAccessReview"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="authorization.k8s.io", kind="LocalSubjectAccessReview", version="v1"
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
    ] = "LocalSubjectAccessReview"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1SubjectAccessReviewSpec,
        Field(
            description="""Spec holds information about the request being evaluated.  spec.namespace must be equal to the namespace you made the request against.  If empty, it is defaulted."""
        ),
    ]

    status: Annotated[
        V1SubjectAccessReviewStatus | None,
        Field(
            description="""Status is filled in by the server and indicates whether the request is allowed or not""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
