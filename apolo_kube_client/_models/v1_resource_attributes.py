from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_field_selector_attributes import V1FieldSelectorAttributes
from .v1_label_selector_attributes import V1LabelSelectorAttributes
from pydantic import BeforeValidator

__all__ = ("V1ResourceAttributes",)


class V1ResourceAttributes(BaseModel):
    """ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.ResourceAttributes"
    )

    field_selector: Annotated[
        V1FieldSelectorAttributes,
        Field(
            alias="fieldSelector",
            description="""fieldSelector describes the limitation on access based on field.  It can only limit access, not broaden it.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1FieldSelectorAttributes)),
    ] = V1FieldSelectorAttributes()

    group: Annotated[
        str | None,
        Field(
            description="""Group is the API Group of the Resource.  "*" means all.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    label_selector: Annotated[
        V1LabelSelectorAttributes,
        Field(
            alias="labelSelector",
            description="""labelSelector describes the limitation on access based on labels.  It can only limit access, not broaden it.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LabelSelectorAttributes)),
    ] = V1LabelSelectorAttributes()

    name: Annotated[
        str | None,
        Field(
            description="""Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    namespace: Annotated[
        str | None,
        Field(
            description="""Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource: Annotated[
        str | None,
        Field(
            description="""Resource is one of the existing resource types.  "*" means all.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    subresource: Annotated[
        str | None,
        Field(
            description="""Subresource is one of the existing resource types.  "" means none.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    verb: Annotated[
        str | None,
        Field(
            description="""Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    version: Annotated[
        str | None,
        Field(
            description="""Version is the API Version of the Resource.  "*" means all.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
