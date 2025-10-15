from pydantic import BaseModel, Field

from .v1alpha3_device_class_configuration import V1alpha3DeviceClassConfiguration
from .v1alpha3_device_selector import V1alpha3DeviceSelector


class V1alpha3DeviceClassSpec(BaseModel):
    config: list[V1alpha3DeviceClassConfiguration] | None = Field(None, alias="config")

    selectors: list[V1alpha3DeviceSelector] | None = Field(None, alias="selectors")
