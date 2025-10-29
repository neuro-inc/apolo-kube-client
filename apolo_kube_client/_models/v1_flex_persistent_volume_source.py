from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator

__all__ = ("V1FlexPersistentVolumeSource",)


class V1FlexPersistentVolumeSource(BaseModel):
    """FlexPersistentVolumeSource represents a generic persistent volume resource that is provisioned/attached using an exec based plugin."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.FlexPersistentVolumeSource"
    )

    driver: Annotated[
        str,
        Field(
            description="""driver is the name of the driver to use for this volume."""
        ),
    ]

    fs_type: Annotated[
        str | None,
        Field(
            alias="fsType",
            description="""fsType is the Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    options: Annotated[
        dict[str, str],
        Field(
            description="""options is Optional: this field holds extra command options if any.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_ref: Annotated[
        V1SecretReference,
        Field(
            alias="secretRef",
            description="""secretRef is Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretReference)),
    ] = V1SecretReference()
