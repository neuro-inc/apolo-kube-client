from pydantic import AliasChoices, BaseModel, Field
from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes

__all__ = ("V1SelfSubjectAccessReviewSpec",)


class V1SelfSubjectAccessReviewSpec(BaseModel):
    non_resource_attributes: V1NonResourceAttributes = Field(
        default_factory=lambda: V1NonResourceAttributes(),
        serialization_alias="nonResourceAttributes",
        validation_alias=AliasChoices(
            "non_resource_attributes", "nonResourceAttributes"
        ),
    )

    resource_attributes: V1ResourceAttributes = Field(
        default_factory=lambda: V1ResourceAttributes(),
        serialization_alias="resourceAttributes",
        validation_alias=AliasChoices("resource_attributes", "resourceAttributes"),
    )
