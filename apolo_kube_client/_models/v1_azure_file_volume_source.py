from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1AzureFileVolumeSource",)


class V1AzureFileVolumeSource(BaseModel):
    """AzureFile represents an Azure File Service mount on the host and bind mount to the pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

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
