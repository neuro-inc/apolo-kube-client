from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1StatefulSetPersistentVolumeClaimRetentionPolicy",)


class V1StatefulSetPersistentVolumeClaimRetentionPolicy(BaseModel):
    """StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.apps.v1.StatefulSetPersistentVolumeClaimRetentionPolicy"
    )

    when_deleted: Annotated[
        str | None,
        Field(
            alias="whenDeleted",
            description="""WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    when_scaled: Annotated[
        str | None,
        Field(
            alias="whenScaled",
            description="""WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
