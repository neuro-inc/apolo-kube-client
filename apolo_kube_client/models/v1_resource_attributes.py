from pydantic import BaseModel, Field

from .v1_field_selector_attributes import V1FieldSelectorAttributes
from .v1_label_selector_attributes import V1LabelSelectorAttributes


class V1ResourceAttributes(BaseModel):
    field_selector: V1FieldSelectorAttributes | None = Field(
        None, alias="fieldSelector"
    )

    group: str | None = Field(None, alias="group")

    label_selector: V1LabelSelectorAttributes | None = Field(
        None, alias="labelSelector"
    )

    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    resource: str | None = Field(None, alias="resource")

    subresource: str | None = Field(None, alias="subresource")

    verb: str | None = Field(None, alias="verb")

    version: str | None = Field(None, alias="version")
