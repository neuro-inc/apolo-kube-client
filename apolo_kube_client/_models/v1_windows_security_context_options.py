from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1WindowsSecurityContextOptions",)


class V1WindowsSecurityContextOptions(BaseModel):
    gmsa_credential_spec: str | None = Field(
        default=None,
        serialization_alias="gmsaCredentialSpec",
        validation_alias=AliasChoices("gmsa_credential_spec", "gmsaCredentialSpec"),
        exclude_if=_exclude_if,
    )

    gmsa_credential_spec_name: str | None = Field(
        default=None,
        serialization_alias="gmsaCredentialSpecName",
        validation_alias=AliasChoices(
            "gmsa_credential_spec_name", "gmsaCredentialSpecName"
        ),
        exclude_if=_exclude_if,
    )

    host_process: bool | None = Field(
        default=None,
        serialization_alias="hostProcess",
        validation_alias=AliasChoices("host_process", "hostProcess"),
        exclude_if=_exclude_if,
    )

    run_as_user_name: str | None = Field(
        default=None,
        serialization_alias="runAsUserName",
        validation_alias=AliasChoices("run_as_user_name", "runAsUserName"),
        exclude_if=_exclude_if,
    )
