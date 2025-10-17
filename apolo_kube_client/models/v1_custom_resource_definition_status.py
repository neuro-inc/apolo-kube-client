from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_custom_resource_definition_condition import V1CustomResourceDefinitionCondition
from .v1_custom_resource_definition_names import V1CustomResourceDefinitionNames

__all__ = ("V1CustomResourceDefinitionStatus",)


class V1CustomResourceDefinitionStatus(BaseModel):
    accepted_names: V1CustomResourceDefinitionNames = Field(
        default_factory=lambda: V1CustomResourceDefinitionNames(), alias="acceptedNames"
    )

    conditions: list[V1CustomResourceDefinitionCondition] = Field(
        default_factory=lambda: []
    )

    stored_versions: list[str] = Field(
        default_factory=lambda: [], alias="storedVersions"
    )
