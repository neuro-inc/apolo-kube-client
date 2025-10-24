from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ScaleSpec",)


class V1ScaleSpec(BaseModel):
    """ScaleSpec describes the attributes of a scale subresource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v1.ScaleSpec"

    replicas: Annotated[
        int | None,
        Field(
            description="""replicas is the desired number of instances for the scaled object.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
