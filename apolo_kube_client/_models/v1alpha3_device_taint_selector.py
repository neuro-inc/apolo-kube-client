from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1alpha3_device_selector import V1alpha3DeviceSelector
from pydantic import BeforeValidator

__all__ = ("V1alpha3DeviceTaintSelector",)


class V1alpha3DeviceTaintSelector(BaseModel):
    """DeviceTaintSelector defines which device(s) a DeviceTaintRule applies to. The empty selector matches all devices. Without a selector, no devices are matched."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1alpha3.DeviceTaintSelector"
    )

    device: Annotated[
        str | None,
        Field(
            description="""If device is set, only devices with that name are selected. This field corresponds to slice.spec.devices[].name.

Setting also driver and pool may be required to avoid ambiguity, but is not required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    device_class_name: Annotated[
        str | None,
        Field(
            alias="deviceClassName",
            description="""If DeviceClassName is set, the selectors defined there must be satisfied by a device to be selected. This field corresponds to class.metadata.name.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    driver: Annotated[
        str | None,
        Field(
            description="""If driver is set, only devices from that driver are selected. This fields corresponds to slice.spec.driver.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    pool: Annotated[
        str | None,
        Field(
            description="""If pool is set, only devices in that pool are selected.

Also setting the driver name may be useful to avoid ambiguity when different drivers use the same pool name, but this is not required because selecting pools from different drivers may also be useful, for example when drivers with node-local devices use the node name as their pool name.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    selectors: Annotated[
        list[V1alpha3DeviceSelector],
        Field(
            description="""Selectors contains the same selection criteria as a ResourceClaim. Currently, CEL expressions are supported. All of these selectors must be satisfied.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
