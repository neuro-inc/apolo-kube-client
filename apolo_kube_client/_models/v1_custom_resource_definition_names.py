from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1CustomResourceDefinitionNames",)


class V1CustomResourceDefinitionNames(BaseModel):
    """CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionNames"
    )

    categories: Annotated[
        list[str],
        Field(
            description="""categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    kind: Annotated[
        str,
        Field(
            description="""kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls."""
        ),
    ]

    list_kind: Annotated[
        str | None,
        Field(
            alias="listKind",
            description="""listKind is the serialized kind of the list for this resource. Defaults to "`kind`List".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    plural: Annotated[
        str,
        Field(
            description="""plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/.../<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase."""
        ),
    ]

    short_names: Annotated[
        list[str],
        Field(
            alias="shortNames",
            description="""shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    singular: Annotated[
        str | None,
        Field(
            description="""singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
