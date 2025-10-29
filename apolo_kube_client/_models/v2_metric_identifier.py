from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator

__all__ = ("V2MetricIdentifier",)


class V2MetricIdentifier(BaseModel):
    """MetricIdentifier defines the name and optionally selector for a metric"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.MetricIdentifier"

    name: Annotated[str, Field(description="""name is the name of the given metric""")]

    selector: Annotated[
        V1LabelSelector,
        Field(
            description="""selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LabelSelector)),
    ] = V1LabelSelector()
