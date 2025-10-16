from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

__all__ = ("V1ManagedFieldsEntry",)


class V1ManagedFieldsEntry(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    fields_type: str | None = Field(None, alias="fieldsType")

    fields_v1: JsonType | None = Field(None, alias="fieldsV1")

    manager: str | None = Field(None, alias="manager")

    operation: str | None = Field(None, alias="operation")

    subresource: str | None = Field(None, alias="subresource")

    time: datetime | None = Field(None, alias="time")
