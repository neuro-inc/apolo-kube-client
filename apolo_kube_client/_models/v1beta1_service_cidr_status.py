from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _collection_if_none
from .v1_condition import V1Condition


__all__ = ("V1beta1ServiceCIDRStatus",)


class V1beta1ServiceCIDRStatus(BaseModel):
    """ServiceCIDRStatus describes the current state of the ServiceCIDR."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.networking.v1beta1.ServiceCIDRStatus"
    )

    conditions: Annotated[
        list[V1Condition],
        Field(
            description="""conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
