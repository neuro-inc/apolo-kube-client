from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ConfigMapNodeConfigSource",)


class V1ConfigMapNodeConfigSource(BaseModel):
    """ConfigMapNodeConfigSource contains the information to reference a ConfigMap as a config source for the Node. This API is deprecated since 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.ConfigMapNodeConfigSource"
    )

    kubelet_config_key: Annotated[
        str,
        Field(
            alias="kubeletConfigKey",
            description="""KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.""",
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""Name is the metadata.name of the referenced ConfigMap. This field is required in all cases."""
        ),
    ]

    namespace: Annotated[
        str,
        Field(
            description="""Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases."""
        ),
    ]

    resource_version: Annotated[
        str | None,
        Field(
            alias="resourceVersion",
            description="""ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    uid: Annotated[
        str | None,
        Field(
            description="""UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
