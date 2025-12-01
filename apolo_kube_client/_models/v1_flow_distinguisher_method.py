from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1FlowDistinguisherMethod",)


class V1FlowDistinguisherMethod(BaseConfiguredModel):
    """FlowDistinguisherMethod specifies the method of a flow distinguisher."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.FlowDistinguisherMethod"
    )

    type: Annotated[
        str,
        Field(
            description="""`type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required."""
        ),
    ]
