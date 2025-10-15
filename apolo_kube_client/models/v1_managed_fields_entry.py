from datetime import datetime

from pydantic import BaseModel, Field

from .object import object


class V1ManagedFieldsEntry(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    fields_type: str | None = Field(None, alias="fieldsType")

    fields_v1: object | None = Field(None, alias="fieldsV1")

    manager: str | None = Field(None, alias="manager")

    operation: str | None = Field(None, alias="operation")

    subresource: str | None = Field(None, alias="subresource")

    time: datetime | None = Field(None, alias="time")
