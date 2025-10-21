from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DownwardAPIVolumeFile",)


class V1DownwardAPIVolumeFile(BaseModel):
    field_ref: Annotated[
        V1ObjectFieldSelector, BeforeValidator(_default_if_none(V1ObjectFieldSelector))
    ] = Field(
        default_factory=lambda: V1ObjectFieldSelector(),
        serialization_alias="fieldRef",
        validation_alias=AliasChoices("field_ref", "fieldRef"),
    )

    mode: int | None = None

    path: str | None = None

    resource_field_ref: Annotated[
        V1ResourceFieldSelector,
        BeforeValidator(_default_if_none(V1ResourceFieldSelector)),
    ] = Field(
        default_factory=lambda: V1ResourceFieldSelector(),
        serialization_alias="resourceFieldRef",
        validation_alias=AliasChoices("resource_field_ref", "resourceFieldRef"),
    )
