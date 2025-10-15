from pydantic import BaseModel, Field

from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes


class V1SelfSubjectAccessReviewSpec(BaseModel):
    non_resource_attributes: V1NonResourceAttributes | None = Field(
        None, alias="nonResourceAttributes"
    )

    resource_attributes: V1ResourceAttributes | None = Field(
        None, alias="resourceAttributes"
    )
