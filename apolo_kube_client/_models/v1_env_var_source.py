from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_config_map_key_selector import V1ConfigMapKeySelector
from .v1_file_key_selector import V1FileKeySelector
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from .v1_secret_key_selector import V1SecretKeySelector

__all__ = ("V1EnvVarSource",)


class V1EnvVarSource(BaseModel):
    """EnvVarSource represents a source for the value of an EnvVar."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EnvVarSource"

    config_map_key_ref: Annotated[
        V1ConfigMapKeySelector | None,
        Field(
            alias="configMapKeyRef",
            description="""Selects a key of a ConfigMap.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    field_ref: Annotated[
        V1ObjectFieldSelector | None,
        Field(
            alias="fieldRef",
            description="""Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    file_key_ref: Annotated[
        V1FileKeySelector | None,
        Field(
            alias="fileKeyRef",
            description="""FileKeyRef selects a key of the env file. Requires the EnvFiles feature gate to be enabled.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource_field_ref: Annotated[
        V1ResourceFieldSelector | None,
        Field(
            alias="resourceFieldRef",
            description="""Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_key_ref: Annotated[
        V1SecretKeySelector | None,
        Field(
            alias="secretKeyRef",
            description="""Selects a key of a secret in the pod's namespace""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
