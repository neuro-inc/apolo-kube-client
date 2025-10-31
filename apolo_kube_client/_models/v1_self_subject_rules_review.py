from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_rules_review_spec import V1SelfSubjectRulesReviewSpec
from .v1_subject_rules_review_status import V1SubjectRulesReviewStatus
from pydantic import BeforeValidator

__all__ = ("V1SelfSubjectRulesReview",)


class V1SelfSubjectRulesReview(ResourceModel):
    """SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server's authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.SelfSubjectRulesReview"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="authorization.k8s.io", kind="SelfSubjectRulesReview", version="v1"
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
    ] = "SelfSubjectRulesReview"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1SelfSubjectRulesReviewSpec,
        Field(
            description="""Spec holds information about the request being evaluated."""
        ),
    ]

    status: Annotated[
        V1SubjectRulesReviewStatus | None,
        Field(
            description="""Status is filled in by the server and indicates the set of actions a user can perform.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
