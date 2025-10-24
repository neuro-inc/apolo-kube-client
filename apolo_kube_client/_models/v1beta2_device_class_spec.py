from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1beta2_device_class_configuration import V1beta2DeviceClassConfiguration
from .v1beta2_device_selector import V1beta2DeviceSelector
from pydantic import BeforeValidator

__all__ = ("V1beta2DeviceClassSpec",)


class V1beta2DeviceClassSpec(BaseModel):
    """DeviceClassSpec is used in a [DeviceClass] to define what can be allocated and how to configure it."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.DeviceClassSpec"

    config: Annotated[
        list[V1beta2DeviceClassConfiguration],
        Field(
            description="""Config defines configuration parameters that apply to each device that is claimed via this class. Some classses may potentially be satisfied by multiple drivers, so each instance of a vendor configuration applies to exactly one driver.

They are passed to the driver, but are not considered while allocating the claim.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    extended_resource_name: Annotated[
        str | None,
        Field(
            alias="extendedResourceName",
            description="""ExtendedResourceName is the extended resource name for the devices of this class. The devices of this class can be used to satisfy a pod's extended resource requests. It has the same format as the name of a pod's extended resource. It should be unique among all the device classes in a cluster. If two device classes have the same name, then the class created later is picked to satisfy a pod's extended resource requests. If two classes are created at the same time, then the name of the class lexicographically sorted first is picked.

This is an alpha field.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    selectors: Annotated[
        list[V1beta2DeviceSelector],
        Field(
            description="""Each selector must be satisfied by a device which is claimed via this class.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
