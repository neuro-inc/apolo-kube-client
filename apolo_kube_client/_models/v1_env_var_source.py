from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_config_map_key_selector import V1ConfigMapKeySelector
from .v1_file_key_selector import V1FileKeySelector
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from .v1_secret_key_selector import V1SecretKeySelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EnvVarSource",)


class V1EnvVarSource(BaseModel):
    config_map_key_ref: Annotated[
        V1ConfigMapKeySelector,
        BeforeValidator(_default_if_none(V1ConfigMapKeySelector)),
    ] = Field(
        default_factory=lambda: V1ConfigMapKeySelector(),
        serialization_alias="configMapKeyRef",
        validation_alias=AliasChoices("config_map_key_ref", "configMapKeyRef"),
        exclude_if=_exclude_if,
    )

    field_ref: Annotated[
        V1ObjectFieldSelector, BeforeValidator(_default_if_none(V1ObjectFieldSelector))
    ] = Field(
        default_factory=lambda: V1ObjectFieldSelector(),
        serialization_alias="fieldRef",
        validation_alias=AliasChoices("field_ref", "fieldRef"),
        exclude_if=_exclude_if,
    )

    file_key_ref: Annotated[
        V1FileKeySelector, BeforeValidator(_default_if_none(V1FileKeySelector))
    ] = Field(
        default_factory=lambda: V1FileKeySelector(),
        serialization_alias="fileKeyRef",
        validation_alias=AliasChoices("file_key_ref", "fileKeyRef"),
        exclude_if=_exclude_if,
    )

    resource_field_ref: Annotated[
        V1ResourceFieldSelector,
        BeforeValidator(_default_if_none(V1ResourceFieldSelector)),
    ] = Field(
        default_factory=lambda: V1ResourceFieldSelector(),
        serialization_alias="resourceFieldRef",
        validation_alias=AliasChoices("resource_field_ref", "resourceFieldRef"),
        exclude_if=_exclude_if,
    )

    secret_key_ref: Annotated[
        V1SecretKeySelector, BeforeValidator(_default_if_none(V1SecretKeySelector))
    ] = Field(
        default_factory=lambda: V1SecretKeySelector(),
        serialization_alias="secretKeyRef",
        validation_alias=AliasChoices("secret_key_ref", "secretKeyRef"),
        exclude_if=_exclude_if,
    )
