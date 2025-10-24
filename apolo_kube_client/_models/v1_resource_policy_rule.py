from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1ResourcePolicyRule",)


class V1ResourcePolicyRule(BaseModel):
    """ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) either (d1) the request does not specify a namespace (i.e., `Namespace==""`) and clusterScope is true or (d2) the request specifies a namespace and least one member of namespaces matches the request's namespace."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.ResourcePolicyRule"
    )

    api_groups: Annotated[
        list[str],
        Field(
            alias="apiGroups",
            description="""`apiGroups` is a list of matching API groups and may not be empty. "*" matches all API groups and, if present, must be the only entry. Required.""",
        ),
    ]

    cluster_scope: Annotated[
        bool | None,
        Field(
            alias="clusterScope",
            description="""`clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    namespaces: Annotated[
        list[str],
        Field(
            description="""`namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "*".  Note that "*" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resources: Annotated[
        list[str],
        Field(
            description="""`resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ "services", "nodes/status" ].  This list may not be empty. "*" matches all resources and, if present, must be the only entry. Required."""
        ),
    ]

    verbs: Annotated[
        list[str],
        Field(
            description="""`verbs` is a list of matching verbs and may not be empty. "*" matches all verbs and, if present, must be the only entry. Required."""
        ),
    ]
