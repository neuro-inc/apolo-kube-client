from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_secret_reference import V1SecretReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FlexPersistentVolumeSource",)


class V1FlexPersistentVolumeSource(BaseModel):
    driver: str | None = None

    fs_type: str | None = Field(
        default=None,
        serialization_alias="fsType",
        validation_alias=AliasChoices("fs_type", "fsType"),
    )

    options: dict[str, str] = {}

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )

    secret_ref: Annotated[
        V1SecretReference, BeforeValidator(_default_if_none(V1SecretReference))
    ] = Field(
        default_factory=lambda: V1SecretReference(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )
