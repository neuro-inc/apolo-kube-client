from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_field_selector_attributes import V1FieldSelectorAttributes
from .v1_label_selector_attributes import V1LabelSelectorAttributes
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceAttributes",)


class V1ResourceAttributes(BaseModel):
    field_selector: Annotated[
        V1FieldSelectorAttributes,
        BeforeValidator(_default_if_none(V1FieldSelectorAttributes)),
    ] = Field(
        default_factory=lambda: V1FieldSelectorAttributes(),
        serialization_alias="fieldSelector",
        validation_alias=AliasChoices("field_selector", "fieldSelector"),
    )

    group: str | None = None

    label_selector: Annotated[
        V1LabelSelectorAttributes,
        BeforeValidator(_default_if_none(V1LabelSelectorAttributes)),
    ] = Field(
        default_factory=lambda: V1LabelSelectorAttributes(),
        serialization_alias="labelSelector",
        validation_alias=AliasChoices("label_selector", "labelSelector"),
    )

    name: str | None = None

    namespace: str | None = None

    resource: str | None = None

    subresource: str | None = None

    verb: str | None = None

    version: str | None = None
