from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1AzureFilePersistentVolumeSource",)


class V1AzureFilePersistentVolumeSource(BaseModel):
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.AzureFilePersistentVolumeSource"
    )

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_name: Annotated[
        str,
        Field(
            alias="secretName",
            description="""secretName is the name of secret that contains Azure Storage Account Name and Key""",
        ),
    ]

    secret_namespace: Annotated[
        str | None,
        Field(
            alias="secretNamespace",
            description="""secretNamespace is the namespace of the secret that contains Azure Storage Account Name and Key default is the same as the Pod""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    share_name: Annotated[
        str,
        Field(alias="shareName", description="""shareName is the azure Share Name"""),
    ]
