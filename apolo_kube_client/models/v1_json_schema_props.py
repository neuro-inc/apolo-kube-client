from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_external_documentation import V1ExternalDocumentation
from .v1_validation_rule import V1ValidationRule
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1JSONSchemaProps",)


class V1JSONSchemaProps(BaseModel):
    ref: str | None = Field(
        default=None,
        serialization_alias="$ref",
        validation_alias=AliasChoices("ref", "$ref"),
    )

    schema_: str | None = Field(
        default=None,
        serialization_alias="$schema",
        validation_alias=AliasChoices("schema_", "$schema"),
    )

    additional_items: JsonType = Field(
        default={},
        serialization_alias="additionalItems",
        validation_alias=AliasChoices("additional_items", "additionalItems"),
    )

    additional_properties: JsonType = Field(
        default={},
        serialization_alias="additionalProperties",
        validation_alias=AliasChoices("additional_properties", "additionalProperties"),
    )

    all_of: list[V1JSONSchemaProps] = Field(
        default=[],
        serialization_alias="allOf",
        validation_alias=AliasChoices("all_of", "allOf"),
    )

    any_of: list[V1JSONSchemaProps] = Field(
        default=[],
        serialization_alias="anyOf",
        validation_alias=AliasChoices("any_of", "anyOf"),
    )

    default: JsonType = Field(default={})

    definitions: dict[str, V1JSONSchemaProps] = Field(default={})

    dependencies: dict[str, JsonType] = Field(default={})

    description: str | None = Field(default=None)

    enum: list[JsonType] = Field(default=[])

    example: JsonType = Field(default={})

    exclusive_maximum: bool | None = Field(
        default=None,
        serialization_alias="exclusiveMaximum",
        validation_alias=AliasChoices("exclusive_maximum", "exclusiveMaximum"),
    )

    exclusive_minimum: bool | None = Field(
        default=None,
        serialization_alias="exclusiveMinimum",
        validation_alias=AliasChoices("exclusive_minimum", "exclusiveMinimum"),
    )

    external_docs: V1ExternalDocumentation = Field(
        default_factory=lambda: V1ExternalDocumentation(),
        serialization_alias="externalDocs",
        validation_alias=AliasChoices("external_docs", "externalDocs"),
    )

    format: str | None = Field(default=None)

    id: str | None = Field(default=None)

    items: JsonType = Field(default={})

    max_items: int | None = Field(
        default=None,
        serialization_alias="maxItems",
        validation_alias=AliasChoices("max_items", "maxItems"),
    )

    max_length: int | None = Field(
        default=None,
        serialization_alias="maxLength",
        validation_alias=AliasChoices("max_length", "maxLength"),
    )

    max_properties: int | None = Field(
        default=None,
        serialization_alias="maxProperties",
        validation_alias=AliasChoices("max_properties", "maxProperties"),
    )

    maximum: float | None = Field(default=None)

    min_items: int | None = Field(
        default=None,
        serialization_alias="minItems",
        validation_alias=AliasChoices("min_items", "minItems"),
    )

    min_length: int | None = Field(
        default=None,
        serialization_alias="minLength",
        validation_alias=AliasChoices("min_length", "minLength"),
    )

    min_properties: int | None = Field(
        default=None,
        serialization_alias="minProperties",
        validation_alias=AliasChoices("min_properties", "minProperties"),
    )

    minimum: float | None = Field(default=None)

    multiple_of: float | None = Field(
        default=None,
        serialization_alias="multipleOf",
        validation_alias=AliasChoices("multiple_of", "multipleOf"),
    )

    not_: V1JSONSchemaProps = Field(
        default_factory=lambda: V1JSONSchemaProps(),
        serialization_alias="not",
        validation_alias=AliasChoices("not_", "not"),
    )

    nullable: bool | None = Field(default=None)

    one_of: list[V1JSONSchemaProps] = Field(
        default=[],
        serialization_alias="oneOf",
        validation_alias=AliasChoices("one_of", "oneOf"),
    )

    pattern: str | None = Field(default=None)

    pattern_properties: dict[str, V1JSONSchemaProps] = Field(
        default={},
        serialization_alias="patternProperties",
        validation_alias=AliasChoices("pattern_properties", "patternProperties"),
    )

    properties: dict[str, V1JSONSchemaProps] = Field(default={})

    required: list[str] = Field(default=[])

    title: str | None = Field(default=None)

    type: str | None = Field(default=None)

    unique_items: bool | None = Field(
        default=None,
        serialization_alias="uniqueItems",
        validation_alias=AliasChoices("unique_items", "uniqueItems"),
    )

    x_kubernetes_embedded_resource: bool | None = Field(
        default=None,
        serialization_alias="x-kubernetes-embedded-resource",
        validation_alias=AliasChoices(
            "x_kubernetes_embedded_resource", "x-kubernetes-embedded-resource"
        ),
    )

    x_kubernetes_int_or_string: bool | None = Field(
        default=None,
        serialization_alias="x-kubernetes-int-or-string",
        validation_alias=AliasChoices(
            "x_kubernetes_int_or_string", "x-kubernetes-int-or-string"
        ),
    )

    x_kubernetes_list_map_keys: list[str] = Field(
        default=[],
        serialization_alias="x-kubernetes-list-map-keys",
        validation_alias=AliasChoices(
            "x_kubernetes_list_map_keys", "x-kubernetes-list-map-keys"
        ),
    )

    x_kubernetes_list_type: str | None = Field(
        default=None,
        serialization_alias="x-kubernetes-list-type",
        validation_alias=AliasChoices(
            "x_kubernetes_list_type", "x-kubernetes-list-type"
        ),
    )

    x_kubernetes_map_type: str | None = Field(
        default=None,
        serialization_alias="x-kubernetes-map-type",
        validation_alias=AliasChoices("x_kubernetes_map_type", "x-kubernetes-map-type"),
    )

    x_kubernetes_preserve_unknown_fields: bool | None = Field(
        default=None,
        serialization_alias="x-kubernetes-preserve-unknown-fields",
        validation_alias=AliasChoices(
            "x_kubernetes_preserve_unknown_fields",
            "x-kubernetes-preserve-unknown-fields",
        ),
    )

    x_kubernetes_validations: list[V1ValidationRule] = Field(
        default=[],
        serialization_alias="x-kubernetes-validations",
        validation_alias=AliasChoices(
            "x_kubernetes_validations", "x-kubernetes-validations"
        ),
    )
