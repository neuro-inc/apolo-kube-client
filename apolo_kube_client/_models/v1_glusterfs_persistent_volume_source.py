from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1GlusterfsPersistentVolumeSource",)


class V1GlusterfsPersistentVolumeSource(BaseModel):
    endpoints: str | None = Field(default=None, exclude_if=_exclude_if)

    endpoints_namespace: str | None = Field(
        default=None,
        serialization_alias="endpointsNamespace",
        validation_alias=AliasChoices("endpoints_namespace", "endpointsNamespace"),
        exclude_if=_exclude_if,
    )

    path: str | None = Field(default=None, exclude_if=_exclude_if)

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
        exclude_if=_exclude_if,
    )
