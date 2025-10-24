from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ScaleStatus",)


class V1ScaleStatus(BaseModel):
    """ScaleStatus represents the current status of a scale subresource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v1.ScaleStatus"

    replicas: Annotated[
        int,
        Field(
            description="""replicas is the actual number of observed instances of the scaled object."""
        ),
    ]

    selector: Annotated[
        str | None,
        Field(
            description="""selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
