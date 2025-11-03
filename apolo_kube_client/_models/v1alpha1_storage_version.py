from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_status import V1alpha1StorageVersionStatus
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator

__all__ = ("V1alpha1StorageVersion",)


class V1alpha1StorageVersion(ResourceModel):
    """Storage version of a specific resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.apiserverinternal.v1alpha1.StorageVersion"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="internal.apiserver.k8s.io", kind="StorageVersion", version="v1alpha1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "internal.apiserver.k8s.io/v1alpha1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "StorageVersion"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""The name is <group>.<resource>.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        JsonType,
        Field(
            description="""Spec is an empty spec. It is here to comply with Kubernetes API style."""
        ),
    ]

    status: Annotated[
        V1alpha1StorageVersionStatus,
        Field(
            description="""API server instances report the version they can decode and the version they encode objects to when persisting objects in the backend."""
        ),
    ]
