from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1AzureFileVolumeSource",)


class V1AzureFileVolumeSource(BaseConfiguredModel):
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.AzureFileVolumeSource"

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
            description="""secretName is the  name of secret that contains Azure Storage Account Name and Key""",
        ),
    ]

    share_name: Annotated[
        str,
        Field(alias="shareName", description="""shareName is the azure share Name"""),
    ]
