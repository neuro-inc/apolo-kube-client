from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_custom_resource_column_definition import V1CustomResourceColumnDefinition
from .v1_custom_resource_subresources import V1CustomResourceSubresources
from .v1_custom_resource_validation import V1CustomResourceValidation
from .v1_selectable_field import V1SelectableField
from pydantic import BeforeValidator

__all__ = ("V1CustomResourceDefinitionVersion",)


class V1CustomResourceDefinitionVersion(BaseModel):
    """CustomResourceDefinitionVersion describes a version for CRD."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionVersion"
    )

    additional_printer_columns: Annotated[
        list[V1CustomResourceColumnDefinition],
        Field(
            alias="additionalPrinterColumns",
            description="""additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    deprecated: Annotated[
        bool | None,
        Field(
            description="""deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    deprecation_warning: Annotated[
        str | None,
        Field(
            alias="deprecationWarning",
            description="""deprecationWarning overrides the default warning returned to API clients. May only be set when `deprecated` is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str,
        Field(
            description="""name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true."""
        ),
    ]

    schema_: Annotated[
        V1CustomResourceValidation,
        Field(
            alias="schema",
            description="""schema describes the schema used for validation, pruning, and defaulting of this version of the custom resource.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1CustomResourceValidation)),
    ] = V1CustomResourceValidation()

    selectable_fields: Annotated[
        list[V1SelectableField],
        Field(
            alias="selectableFields",
            description="""selectableFields specifies paths to fields that may be used as field selectors. A maximum of 8 selectable fields are allowed. See https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    served: Annotated[
        bool,
        Field(
            description="""served is a flag enabling/disabling this version from being served via REST APIs"""
        ),
    ]

    storage: Annotated[
        bool,
        Field(
            description="""storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true."""
        ),
    ]

    subresources: Annotated[
        V1CustomResourceSubresources,
        Field(
            description="""subresources specify what subresources this version of the defined custom resource have.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1CustomResourceSubresources)),
    ] = V1CustomResourceSubresources()
