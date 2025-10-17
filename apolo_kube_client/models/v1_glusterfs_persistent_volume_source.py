from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1GlusterfsPersistentVolumeSource",)


class V1GlusterfsPersistentVolumeSource(BaseModel):
    endpoints: str | None = None

    endpoints_namespace: str | None = Field(
        default=None,
        serialization_alias="endpointsNamespace",
        validation_alias=AliasChoices("endpoints_namespace", "endpointsNamespace"),
    )

    path: str | None = None

    read_only: bool | None = Field(
        default=None,
        serialization_alias="readOnly",
        validation_alias=AliasChoices("read_only", "readOnly"),
    )
