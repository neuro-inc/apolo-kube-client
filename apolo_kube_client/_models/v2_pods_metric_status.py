from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2PodsMetricStatus",)


class V2PodsMetricStatus(BaseModel):
    """PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.PodsMetricStatus"

    current: Annotated[
        V2MetricValueStatus,
        Field(
            description="""current contains the current value for the given metric"""
        ),
    ]

    metric: Annotated[
        V2MetricIdentifier,
        Field(
            description="""metric identifies the target metric by name and selector"""
        ),
    ]
