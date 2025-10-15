from pydantic import BaseModel, Field

from .v1alpha3_basic_device import V1alpha3BasicDevice


class V1alpha3Device(BaseModel):
    basic: V1alpha3BasicDevice | None = Field(None, alias="basic")

    name: str | None = Field(None, alias="name")
