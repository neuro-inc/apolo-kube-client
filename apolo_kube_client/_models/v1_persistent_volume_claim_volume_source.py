from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PersistentVolumeClaimVolumeSource",)


class V1PersistentVolumeClaimVolumeSource(BaseModel):
    """PersistentVolumeClaimVolumeSource references the user's PVC in the same namespace. This volume finds the bound PV and mounts that volume for the pod. A PersistentVolumeClaimVolumeSource is, essentially, a wrapper around another type of volume that is owned by someone else (the system)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.PersistentVolumeClaimVolumeSource"
    )

    claim_name: Annotated[
        str,
        Field(
            alias="claimName",
            description="""claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims""",
        ),
    ]

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly Will force the ReadOnly setting in VolumeMounts. Default false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
