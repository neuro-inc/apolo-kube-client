from pydantic import BaseModel, Field

from .v1_custom_resource_definition_condition import V1CustomResourceDefinitionCondition
from .v1_custom_resource_definition_names import V1CustomResourceDefinitionNames


class V1CustomResourceDefinitionStatus(BaseModel):
    accepted_names: V1CustomResourceDefinitionNames | None = Field(
        None, alias="acceptedNames"
    )

    conditions: list[V1CustomResourceDefinitionCondition] | None = Field(
        None, alias="conditions"
    )

    stored_versions: list[str] | None = Field(None, alias="storedVersions")
