from pydantic import AliasChoices, BaseModel, Field
from apolo_kube_client._typedefs import JsonType
from datetime import datetime

__all__ = ("V1ManagedFieldsEntry",)


class V1ManagedFieldsEntry(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    fields_type: str | None = Field(
        default=None,
        serialization_alias="fieldsType",
        validation_alias=AliasChoices("fields_type", "fieldsType"),
    )

    fields_v1: JsonType = Field(
        default={},
        serialization_alias="fieldsV1",
        validation_alias=AliasChoices("fields_v1", "fieldsV1"),
    )

    manager: str | None = None

    operation: str | None = None

    subresource: str | None = None

    time: datetime | None = None
