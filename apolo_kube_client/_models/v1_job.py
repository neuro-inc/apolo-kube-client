from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_job_spec import V1JobSpec
from .v1_job_status import V1JobStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Job",)


class V1Job(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[V1JobSpec, BeforeValidator(_default_if_none(V1JobSpec))] = Field(
        default_factory=lambda: V1JobSpec()
    )

    status: Annotated[V1JobStatus, BeforeValidator(_default_if_none(V1JobStatus))] = (
        Field(default_factory=lambda: V1JobStatus())
    )
