from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1_csi_node_driver import V1CSINodeDriver


__all__ = ("V1CSINodeSpec",)


class V1CSINodeSpec(BaseConfiguredModel):
    """CSINodeSpec holds information about the specification of all CSI drivers installed on a node"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.CSINodeSpec"

    drivers: Annotated[
        list[V1CSINodeDriver],
        Field(
            description="""drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty."""
        ),
    ]
