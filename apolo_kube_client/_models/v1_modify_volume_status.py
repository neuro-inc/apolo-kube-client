from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ModifyVolumeStatus",)


class V1ModifyVolumeStatus(BaseModel):
    """ModifyVolumeStatus represents the status object of ControllerModifyVolume operation"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ModifyVolumeStatus"

    status: Annotated[
        str,
        Field(
            description="""status is the status of the ControllerModifyVolume operation. It can be in any of following states:
 - Pending
   Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as
   the specified VolumeAttributesClass not existing.
 - InProgress
   InProgress indicates that the volume is being modified.
 - Infeasible
  Infeasible indicates that the request has been rejected as invalid by the CSI driver. To
	  resolve the error, a valid VolumeAttributesClass needs to be specified.
Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately."""
        ),
    ]

    target_volume_attributes_class_name: Annotated[
        str | None,
        Field(
            alias="targetVolumeAttributesClassName",
            description="""targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
