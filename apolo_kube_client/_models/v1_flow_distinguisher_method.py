from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1FlowDistinguisherMethod",)


class V1FlowDistinguisherMethod(BaseModel):
    """FlowDistinguisherMethod specifies the method of a flow distinguisher."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.FlowDistinguisherMethod"
    )

    type: Annotated[
        str,
        Field(
            description="""`type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required."""
        ),
    ]
