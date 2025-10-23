from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_deployment_spec import V1DeploymentSpec
from .v1_deployment_status import V1DeploymentStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Deployment",)


class V1Deployment(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1DeploymentSpec, BeforeValidator(_default_if_none(V1DeploymentSpec))
    ] = Field(default_factory=lambda: V1DeploymentSpec(), exclude_if=_exclude_if)

    status: Annotated[
        V1DeploymentStatus, BeforeValidator(_default_if_none(V1DeploymentStatus))
    ] = Field(default_factory=lambda: V1DeploymentStatus(), exclude_if=_exclude_if)
