from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1AzureFilePersistentVolumeSource",)


class V1AzureFilePersistentVolumeSource(BaseModel):
    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )

    secret_name: str | None = Field(
        default=None,
        serialization_alias="secretName",
        validation_alias=AliasChoices("secret_name", "secretName"),
        exclude_if=_exclude_if,
    )

    secret_namespace: str | None = Field(
        default=None,
        serialization_alias="secretNamespace",
        validation_alias=AliasChoices("secret_namespace", "secretNamespace"),
        exclude_if=_exclude_if,
    )

    share_name: str | None = Field(
        default=None,
        serialization_alias="shareName",
        validation_alias=AliasChoices("share_name", "shareName"),
        exclude_if=_exclude_if,
    )
