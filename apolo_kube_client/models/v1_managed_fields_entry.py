from __future__ import annotations
from pydantic import BaseModel, Field
from apolo_kube_client._typedefs import JsonType
from datetime import datetime

__all__ = ("V1ManagedFieldsEntry",)


class V1ManagedFieldsEntry(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    fields_type: str | None = Field(default_factory=lambda: None, alias="fieldsType")

    fields_v1: JsonType = Field(default_factory=lambda: {}, alias="fieldsV1")

    manager: str | None = Field(default_factory=lambda: None, alias="manager")

    operation: str | None = Field(default_factory=lambda: None, alias="operation")

    subresource: str | None = Field(default_factory=lambda: None, alias="subresource")

    time: datetime | None = Field(default_factory=lambda: None, alias="time")
