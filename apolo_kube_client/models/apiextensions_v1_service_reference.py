from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("ApiextensionsV1ServiceReference",)


class ApiextensionsV1ServiceReference(BaseModel):
    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    path: str | None = Field(None, alias="path")

    port: int | None = Field(None, alias="port")
