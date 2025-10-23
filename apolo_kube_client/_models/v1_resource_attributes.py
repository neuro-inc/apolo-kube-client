from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    group: str | None = Field(default=None, exclude_if=_exclude_if)

    label_selector: Annotated[
        V1LabelSelectorAttributes,
        BeforeValidator(_default_if_none(V1LabelSelectorAttributes)),
    ] = Field(
        default_factory=lambda: V1LabelSelectorAttributes(),
        serialization_alias="labelSelector",
        validation_alias=AliasChoices("label_selector", "labelSelector"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace: str | None = Field(default=None, exclude_if=_exclude_if)

    resource: str | None = Field(default=None, exclude_if=_exclude_if)

    subresource: str | None = Field(default=None, exclude_if=_exclude_if)

    verb: str | None = Field(default=None, exclude_if=_exclude_if)

    version: str | None = Field(default=None, exclude_if=_exclude_if)
