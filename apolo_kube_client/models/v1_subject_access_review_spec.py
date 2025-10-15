from pydantic import BaseModel, Field

from .v1_non_resource_attributes import V1NonResourceAttributes
from .v1_resource_attributes import V1ResourceAttributes


class V1SubjectAccessReviewSpec(BaseModel):
    extra: dict(str, list[str]) | None = Field(None, alias="extra")

    groups: list[str] | None = Field(None, alias="groups")

    non_resource_attributes: V1NonResourceAttributes | None = Field(
        None, alias="nonResourceAttributes"
    )

    resource_attributes: V1ResourceAttributes | None = Field(
        None, alias="resourceAttributes"
    )

    uid: str | None = Field(None, alias="uid")

    user: str | None = Field(None, alias="user")
