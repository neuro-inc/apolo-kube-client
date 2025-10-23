from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ConfigMapNodeConfigSource",)


class V1ConfigMapNodeConfigSource(BaseModel):
    kubelet_config_key: str | None = Field(
        default=None,
        serialization_alias="kubeletConfigKey",
        validation_alias=AliasChoices("kubelet_config_key", "kubeletConfigKey"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace: str | None = Field(default=None, exclude_if=_exclude_if)

    resource_version: str | None = Field(
        default=None,
        serialization_alias="resourceVersion",
        validation_alias=AliasChoices("resource_version", "resourceVersion"),
        exclude_if=_exclude_if,
    )

    uid: str | None = Field(default=None, exclude_if=_exclude_if)
