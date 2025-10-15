from pydantic import BaseModel, Field

from .v1beta1_parent_reference import V1beta1ParentReference


class V1beta1IPAddressSpec(BaseModel):
    parent_ref: V1beta1ParentReference | None = Field(None, alias="parentRef")
