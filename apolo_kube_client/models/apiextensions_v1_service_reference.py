from pydantic import BaseModel, Field


class ApiextensionsV1ServiceReference(BaseModel):
    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    path: str | None = Field(None, alias="path")

    port: int | None = Field(None, alias="port")
