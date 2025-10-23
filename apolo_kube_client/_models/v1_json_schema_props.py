from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_external_documentation import V1ExternalDocumentation
from .v1_validation_rule import V1ValidationRule
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1JSONSchemaProps",)


class V1JSONSchemaProps(BaseModel):
    ref: str | None = Field(
        default=None,
        serialization_alias="$ref",
        validation_alias=AliasChoices("ref", "$ref"),
        exclude_if=_exclude_if,
    )

    schema_: str | None = Field(
        default=None,
        serialization_alias="$schema",
        validation_alias=AliasChoices("schema_", "$schema"),
        exclude_if=_exclude_if,
    )

    additional_items: JsonType = Field(
        default={},
        serialization_alias="additionalItems",
        validation_alias=AliasChoices("additional_items", "additionalItems"),
        exclude_if=_exclude_if,
    )

    additional_properties: JsonType = Field(
        default={},
        serialization_alias="additionalProperties",
        validation_alias=AliasChoices("additional_properties", "additionalProperties"),
        exclude_if=_exclude_if,
    )

    all_of: Annotated[
        list["V1JSONSchemaProps"], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="allOf",
        validation_alias=AliasChoices("all_of", "allOf"),
        exclude_if=_exclude_if,
    )

    any_of: Annotated[
        list["V1JSONSchemaProps"], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="anyOf",
        validation_alias=AliasChoices("any_of", "anyOf"),
        exclude_if=_exclude_if,
    )

    default: JsonType = Field(default={}, exclude_if=_exclude_if)

    definitions: Annotated[
        dict[str, "V1JSONSchemaProps"], BeforeValidator(_collection_if_none("{}"))
    ] = Field(default={}, exclude_if=_exclude_if)

    dependencies: Annotated[
        dict[str, JsonType], BeforeValidator(_collection_if_none("{}"))
    ] = Field(default={}, exclude_if=_exclude_if)

    description: str | None = Field(default=None, exclude_if=_exclude_if)

    enum: Annotated[list[JsonType], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    example: JsonType = Field(default={}, exclude_if=_exclude_if)

    exclusive_maximum: bool | None = Field(
        default=None,
        serialization_alias="exclusiveMaximum",
        validation_alias=AliasChoices("exclusive_maximum", "exclusiveMaximum"),
        exclude_if=_exclude_if,
    )

    exclusive_minimum: bool | None = Field(
        default=None,
        serialization_alias="exclusiveMinimum",
        validation_alias=AliasChoices("exclusive_minimum", "exclusiveMinimum"),
        exclude_if=_exclude_if,
    )

    external_docs: Annotated[
        V1ExternalDocumentation,
        BeforeValidator(_default_if_none(V1ExternalDocumentation)),
    ] = Field(
        default_factory=lambda: V1ExternalDocumentation(),
        serialization_alias="externalDocs",
        validation_alias=AliasChoices("external_docs", "externalDocs"),
        exclude_if=_exclude_if,
    )

    format: str | None = Field(default=None, exclude_if=_exclude_if)

    id: str | None = Field(default=None, exclude_if=_exclude_if)

    items: JsonType = Field(default={}, exclude_if=_exclude_if)

    max_items: int | None = Field(
        default=None,
        serialization_alias="maxItems",
        validation_alias=AliasChoices("max_items", "maxItems"),
        exclude_if=_exclude_if,
    )

    max_length: int | None = Field(
        default=None,
        serialization_alias="maxLength",
        validation_alias=AliasChoices("max_length", "maxLength"),
        exclude_if=_exclude_if,
    )

    max_properties: int | None = Field(
        default=None,
        serialization_alias="maxProperties",
        validation_alias=AliasChoices("max_properties", "maxProperties"),
        exclude_if=_exclude_if,
    )

    maximum: float | None = Field(default=None, exclude_if=_exclude_if)

    min_items: int | None = Field(
        default=None,
        serialization_alias="minItems",
        validation_alias=AliasChoices("min_items", "minItems"),
        exclude_if=_exclude_if,
    )

    min_length: int | None = Field(
        default=None,
        serialization_alias="minLength",
        validation_alias=AliasChoices("min_length", "minLength"),
        exclude_if=_exclude_if,
    )

    min_properties: int | None = Field(
        default=None,
        serialization_alias="minProperties",
        validation_alias=AliasChoices("min_properties", "minProperties"),
        exclude_if=_exclude_if,
    )

    minimum: float | None = Field(default=None, exclude_if=_exclude_if)

    multiple_of: float | None = Field(
        default=None,
        serialization_alias="multipleOf",
        validation_alias=AliasChoices("multiple_of", "multipleOf"),
        exclude_if=_exclude_if,
    )

    not_: Annotated[
        "V1JSONSchemaProps | None",
        BeforeValidator(_default_if_none("V1JSONSchemaProps | None")),
    ] = Field(
        default=None,
        serialization_alias="not",
        validation_alias=AliasChoices("not_", "not"),
        exclude_if=_exclude_if,
    )

    nullable: bool | None = Field(default=None, exclude_if=_exclude_if)

    one_of: Annotated[
        list["V1JSONSchemaProps"], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="oneOf",
        validation_alias=AliasChoices("one_of", "oneOf"),
        exclude_if=_exclude_if,
    )

    pattern: str | None = Field(default=None, exclude_if=_exclude_if)

    pattern_properties: Annotated[
        dict[str, "V1JSONSchemaProps"], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="patternProperties",
        validation_alias=AliasChoices("pattern_properties", "patternProperties"),
        exclude_if=_exclude_if,
    )

    properties: Annotated[
        dict[str, "V1JSONSchemaProps"], BeforeValidator(_collection_if_none("{}"))
    ] = Field(default={}, exclude_if=_exclude_if)

    required: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    title: str | None = Field(default=None, exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)

    unique_items: bool | None = Field(
        default=None,
        serialization_alias="uniqueItems",
        validation_alias=AliasChoices("unique_items", "uniqueItems"),
        exclude_if=_exclude_if,
    )

    x_kubernetes_embedded_resource: bool | None = Field(
        default=None,
        serialization_alias="x-kubernetes-embedded-resource",
        validation_alias=AliasChoices(
            "x_kubernetes_embedded_resource", "x-kubernetes-embedded-resource"
        ),
        exclude_if=_exclude_if,
    )

    x_kubernetes_int_or_string: bool | None = Field(
        default=None,
        serialization_alias="x-kubernetes-int-or-string",
        validation_alias=AliasChoices(
            "x_kubernetes_int_or_string", "x-kubernetes-int-or-string"
        ),
        exclude_if=_exclude_if,
    )

    x_kubernetes_list_map_keys: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="x-kubernetes-list-map-keys",
        validation_alias=AliasChoices(
            "x_kubernetes_list_map_keys", "x-kubernetes-list-map-keys"
        ),
        exclude_if=_exclude_if,
    )

    x_kubernetes_list_type: str | None = Field(
        default=None,
        serialization_alias="x-kubernetes-list-type",
        validation_alias=AliasChoices(
            "x_kubernetes_list_type", "x-kubernetes-list-type"
        ),
        exclude_if=_exclude_if,
    )

    x_kubernetes_map_type: str | None = Field(
        default=None,
        serialization_alias="x-kubernetes-map-type",
        validation_alias=AliasChoices("x_kubernetes_map_type", "x-kubernetes-map-type"),
        exclude_if=_exclude_if,
    )

    x_kubernetes_preserve_unknown_fields: bool | None = Field(
        default=None,
        serialization_alias="x-kubernetes-preserve-unknown-fields",
        validation_alias=AliasChoices(
            "x_kubernetes_preserve_unknown_fields",
            "x-kubernetes-preserve-unknown-fields",
        ),
        exclude_if=_exclude_if,
    )

    x_kubernetes_validations: Annotated[
        list[V1ValidationRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="x-kubernetes-validations",
        validation_alias=AliasChoices(
            "x_kubernetes_validations", "x-kubernetes-validations"
        ),
        exclude_if=_exclude_if,
    )
