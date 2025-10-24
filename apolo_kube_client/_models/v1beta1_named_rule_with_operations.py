from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1beta1NamedRuleWithOperations",)


class V1beta1NamedRuleWithOperations(BaseModel):
    """NamedRuleWithOperations is a tuple of Operations and Resources with ResourceNames."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1beta1.NamedRuleWithOperations"
    )

    api_groups: Annotated[
        list[str],
        Field(
            alias="apiGroups",
            description="""APIGroups is the API groups the resources belong to. '*' is all groups. If '*' is present, the length of the slice must be one. Required.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    api_versions: Annotated[
        list[str],
        Field(
            alias="apiVersions",
            description="""APIVersions is the API versions the resources belong to. '*' is all versions. If '*' is present, the length of the slice must be one. Required.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    operations: Annotated[
        list[str],
        Field(
            description="""Operations is the operations the admission hook cares about - CREATE, UPDATE, DELETE, CONNECT or * for all of those operations and any future admission operations that are added. If '*' is present, the length of the slice must be one. Required.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resource_names: Annotated[
        list[str],
        Field(
            alias="resourceNames",
            description="""ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resources: Annotated[
        list[str],
        Field(
            description="""Resources is a list of resources this rule applies to.

For example: 'pods' means pods. 'pods/log' means the log subresource of pods. '*' means all resources, but not subresources. 'pods/*' means all subresources of pods. '*/scale' means all scale subresources. '*/*' means all resources and their subresources.

If wildcard is present, the validation rule will ensure resources do not overlap with each other.

Depending on the enclosing object, subresources might not be allowed. Required.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    scope: Annotated[
        str | None,
        Field(
            description="""scope specifies the scope of this rule. Valid values are "Cluster", "Namespaced", and "*" "Cluster" means that only cluster-scoped resources will match this rule. Namespace API objects are cluster-scoped. "Namespaced" means that only namespaced resources will match this rule. "*" means that there are no scope restrictions. Subresources match the scope of their parent resource. Default is "*".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
