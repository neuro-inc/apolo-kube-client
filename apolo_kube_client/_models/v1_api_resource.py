from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1APIResource",)


class V1APIResource(BaseModel):
    """APIResource specifies the name of a resource and whether it is namespaced."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.APIResource"
    )

    categories: Annotated[
        list[str],
        Field(
            description="""categories is a list of the grouped resources this resource belongs to (e.g. 'all')""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    group: Annotated[
        str | None,
        Field(
            description="""group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str,
        Field(
            description="""kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')"""
        ),
    ]

    name: Annotated[
        str, Field(description="""name is the plural name of the resource.""")
    ]

    namespaced: Annotated[
        bool,
        Field(
            description="""namespaced indicates if a resource is namespaced or not."""
        ),
    ]

    short_names: Annotated[
        list[str],
        Field(
            alias="shortNames",
            description="""shortNames is a list of suggested short names of the resource.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    singular_name: Annotated[
        str,
        Field(
            alias="singularName",
            description="""singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.""",
        ),
    ]

    storage_version_hash: Annotated[
        str | None,
        Field(
            alias="storageVersionHash",
            description="""The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    verbs: Annotated[
        list[str],
        Field(
            description="""verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)"""
        ),
    ]

    version: Annotated[
        str | None,
        Field(
            description="""version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
