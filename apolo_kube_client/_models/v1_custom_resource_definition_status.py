from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_custom_resource_definition_condition import V1CustomResourceDefinitionCondition
from .v1_custom_resource_definition_names import V1CustomResourceDefinitionNames
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceDefinitionStatus",)


class V1CustomResourceDefinitionStatus(BaseModel):
    accepted_names: Annotated[
        V1CustomResourceDefinitionNames,
        BeforeValidator(_default_if_none(V1CustomResourceDefinitionNames)),
    ] = Field(
        default_factory=lambda: V1CustomResourceDefinitionNames(),
        serialization_alias="acceptedNames",
        validation_alias=AliasChoices("accepted_names", "acceptedNames"),
    )

    conditions: list[V1CustomResourceDefinitionCondition] = []

    stored_versions: list[str] = Field(
        default=[],
        serialization_alias="storedVersions",
        validation_alias=AliasChoices("stored_versions", "storedVersions"),
    )
