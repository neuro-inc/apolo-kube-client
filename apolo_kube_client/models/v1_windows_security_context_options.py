from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1WindowsSecurityContextOptions",)


class V1WindowsSecurityContextOptions(BaseModel):
    gmsa_credential_spec: str | None = Field(
        default=None,
        serialization_alias="gmsaCredentialSpec",
        validation_alias=AliasChoices("gmsa_credential_spec", "gmsaCredentialSpec"),
    )

    gmsa_credential_spec_name: str | None = Field(
        default=None,
        serialization_alias="gmsaCredentialSpecName",
        validation_alias=AliasChoices(
            "gmsa_credential_spec_name", "gmsaCredentialSpecName"
        ),
    )

    host_process: bool | None = Field(
        default=None,
        serialization_alias="hostProcess",
        validation_alias=AliasChoices("host_process", "hostProcess"),
    )

    run_as_user_name: str | None = Field(
        default=None,
        serialization_alias="runAsUserName",
        validation_alias=AliasChoices("run_as_user_name", "runAsUserName"),
    )
