from pydantic import BaseModel, Field


class V1alpha3DeviceAttribute(BaseModel):
    bool: bool | None = Field(None, alias="bool")

    int: int | None = Field(None, alias="int")

    string: str | None = Field(None, alias="string")

    version: str | None = Field(None, alias="version")
