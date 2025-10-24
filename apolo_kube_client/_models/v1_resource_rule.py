from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1ResourceRule",)


class V1ResourceRule(BaseModel):
    """ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.authorization.v1.ResourceRule"

    api_groups: Annotated[
        list[str],
        Field(
            alias="apiGroups",
            description="""APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resource_names: Annotated[
        list[str],
        Field(
            alias="resourceNames",
            description="""ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    resources: Annotated[
        list[str],
        Field(
            description="""Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.
 "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    verbs: Annotated[
        list[str],
        Field(
            description="""Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all."""
        ),
    ]
