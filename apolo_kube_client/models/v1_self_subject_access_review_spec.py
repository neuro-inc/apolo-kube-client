from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes

__all__ = ("V1SelfSubjectAccessReviewSpec",)


class V1SelfSubjectAccessReviewSpec(BaseModel):
    non_resource_attributes: V1NonResourceAttributes = Field(
        default_factory=lambda: V1NonResourceAttributes(), alias="nonResourceAttributes"
    )

    resource_attributes: V1ResourceAttributes = Field(
        default_factory=lambda: V1ResourceAttributes(), alias="resourceAttributes"
    )
