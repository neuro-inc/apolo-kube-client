from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_job_spec import V1JobSpec
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator

__all__ = ("V1JobTemplateSpec",)


class V1JobTemplateSpec(ResourceModel):
    """JobTemplateSpec describes the data a Job should have when created from a template"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.JobTemplateSpec"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata of the jobs created from this template. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1JobSpec | None,
        Field(
            description="""Specification of the desired behavior of the job. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
