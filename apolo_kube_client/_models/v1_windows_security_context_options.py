from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1WindowsSecurityContextOptions",)


class V1WindowsSecurityContextOptions(BaseModel):
    """WindowsSecurityContextOptions contain Windows-specific options and credentials."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.WindowsSecurityContextOptions"
    )

    gmsa_credential_spec: Annotated[
        str | None,
        Field(
            alias="gmsaCredentialSpec",
            description="""GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    gmsa_credential_spec_name: Annotated[
        str | None,
        Field(
            alias="gmsaCredentialSpecName",
            description="""GMSACredentialSpecName is the name of the GMSA credential spec to use.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    host_process: Annotated[
        bool | None,
        Field(
            alias="hostProcess",
            description="""HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod's containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    run_as_user_name: Annotated[
        str | None,
        Field(
            alias="runAsUserName",
            description="""The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
