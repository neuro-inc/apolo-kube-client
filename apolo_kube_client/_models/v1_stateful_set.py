from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_stateful_set_spec import V1StatefulSetSpec
from .v1_stateful_set_status import V1StatefulSetStatus
from pydantic import BeforeValidator

__all__ = ("V1StatefulSet",)


class V1StatefulSet(ResourceModel):
    """StatefulSet represents a set of pods with consistent identities. Identities are defined as:
      - Network: A single stable DNS and hostname.
      - Storage: As many VolumeClaims as requested.

    The StatefulSet guarantees that a given network identity will always map to the same storage identity."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.StatefulSet"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="apps", kind="StatefulSet", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "apps/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "StatefulSet"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1StatefulSetSpec | None,
        Field(
            description="""Spec defines the desired identities of pods in this set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        V1StatefulSetStatus | None,
        Field(
            description="""Status is the current status of Pods in this StatefulSet. This data may be out of date by some window of time.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
