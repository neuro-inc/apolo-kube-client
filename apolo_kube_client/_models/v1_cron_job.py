from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_cron_job_spec import V1CronJobSpec
from .v1_cron_job_status import V1CronJobStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CronJob",)


class V1CronJob(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[V1CronJobSpec, BeforeValidator(_default_if_none(V1CronJobSpec))] = (
        Field(default_factory=lambda: V1CronJobSpec(), exclude_if=_exclude_if)
    )

    status: Annotated[
        V1CronJobStatus, BeforeValidator(_default_if_none(V1CronJobStatus))
    ] = Field(default_factory=lambda: V1CronJobStatus(), exclude_if=_exclude_if)
