from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from apolo_kube_client._typedefs import JsonType
from datetime import datetime

__all__ = ("V1ManagedFieldsEntry",)


class V1ManagedFieldsEntry(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    fields_type: str | None = Field(
        default=None,
        serialization_alias="fieldsType",
        validation_alias=AliasChoices("fields_type", "fieldsType"),
        exclude_if=_exclude_if,
    )

    fields_v1: JsonType = Field(
        default={},
        serialization_alias="fieldsV1",
        validation_alias=AliasChoices("fields_v1", "fieldsV1"),
        exclude_if=_exclude_if,
    )

    manager: str | None = Field(default=None, exclude_if=_exclude_if)

    operation: str | None = Field(default=None, exclude_if=_exclude_if)

    subresource: str | None = Field(default=None, exclude_if=_exclude_if)

    time: datetime | None = Field(default=None, exclude_if=_exclude_if)
