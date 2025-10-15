from pydantic import BaseModel, Field

from .object import object


class V1beta1OpaqueDeviceConfiguration(BaseModel):
    driver: str | None = Field(None, alias="driver")

    parameters: object | None = Field(None, alias="parameters")
