from pydantic import BaseModel, Field


class V1WindowsSecurityContextOptions(BaseModel):
    gmsa_credential_spec: str | None = Field(None, alias="gmsaCredentialSpec")

    gmsa_credential_spec_name: str | None = Field(None, alias="gmsaCredentialSpecName")

    host_process: bool | None = Field(None, alias="hostProcess")

    run_as_user_name: str | None = Field(None, alias="runAsUserName")
