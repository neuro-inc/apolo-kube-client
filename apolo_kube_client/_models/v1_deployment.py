from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
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
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1DeploymentSpec, BeforeValidator(_default_if_none(V1DeploymentSpec))
    ] = Field(default_factory=lambda: V1DeploymentSpec())

    status: Annotated[
        V1DeploymentStatus, BeforeValidator(_default_if_none(V1DeploymentStatus))
    ] = Field(default_factory=lambda: V1DeploymentStatus())
