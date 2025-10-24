from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1beta1OpaqueDeviceConfiguration",)


class V1beta1OpaqueDeviceConfiguration(BaseModel):
    """OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta1.OpaqueDeviceConfiguration"
    )

    driver: Annotated[
        str,
        Field(
            description="""Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.

An admission policy provided by the driver developer could use this to decide whether it needs to validate them.

Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver."""
        ),
    ]

    parameters: Annotated[
        JsonType,
        Field(
            description="""Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version ("kind" + "apiVersion" for Kubernetes types), with conversion between different versions.

The length of the raw data must be smaller or equal to 10 Ki."""
        ),
    ]
