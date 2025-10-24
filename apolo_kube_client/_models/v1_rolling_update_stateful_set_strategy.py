from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1RollingUpdateStatefulSetStrategy",)


class V1RollingUpdateStatefulSetStrategy(BaseModel):
    """RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.apps.v1.RollingUpdateStatefulSetStrategy"
    )

    max_unavailable: Annotated[
        JsonType,
        Field(
            alias="maxUnavailable",
            description="""The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable.""",
            exclude_if=lambda v: v == {},
        ),
    ] = {}

    partition: Annotated[
        int | None,
        Field(
            description="""Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
