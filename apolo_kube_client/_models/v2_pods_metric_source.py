from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget

__all__ = ("V2PodsMetricSource",)


class V2PodsMetricSource(BaseModel):
    """PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.PodsMetricSource"

    metric: Annotated[
        V2MetricIdentifier,
        Field(
            description="""metric identifies the target metric by name and selector"""
        ),
    ]

    target: Annotated[
        V2MetricTarget,
        Field(description="""target specifies the target value for the given metric"""),
    ]
