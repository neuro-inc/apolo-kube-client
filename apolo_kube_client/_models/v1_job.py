from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_job_spec import V1JobSpec
from .v1_job_status import V1JobStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator

__all__ = ("V1Job",)


class V1Job(ResourceModel):
    """Job represents the configuration of a single job."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.Job"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="batch", kind="Job", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "batch/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "Job"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1JobSpec | None,
        Field(
            description="""Specification of the desired behavior of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        V1JobStatus,
        Field(
            description="""Current status of a job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1JobStatus)),
    ] = V1JobStatus()
