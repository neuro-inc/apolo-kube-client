from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("ApiregistrationV1ServiceReference",)


class ApiregistrationV1ServiceReference(BaseModel):
    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    port: int | None = Field(None, alias="port")
