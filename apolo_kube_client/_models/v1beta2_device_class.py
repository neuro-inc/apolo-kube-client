from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1beta2_device_class_spec import V1beta2DeviceClassSpec
from pydantic import BeforeValidator

__all__ = ("V1beta2DeviceClass",)


class V1beta2DeviceClass(ResourceModel):
    """DeviceClass is a vendor- or admin-provided resource that contains device configuration and selectors. It can be referenced in the device requests of a claim to apply these presets. Cluster scoped.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate."""

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.DeviceClass"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="resource.k8s.io", kind="DeviceClass", version="v1beta2"
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str | None,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata""",
            exclude_if=lambda v: v == V1ObjectMeta(),
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1beta2DeviceClassSpec,
        Field(
            description="""Spec defines what can be allocated and how to configure it.

This is mutable. Consumers have to be prepared for classes changing at any time, either because they get updated or replaced. Claim allocations are done once based on whatever was set in classes at the time of allocation.

Changing the spec automatically increments the metadata.generation number."""
        ),
    ]
