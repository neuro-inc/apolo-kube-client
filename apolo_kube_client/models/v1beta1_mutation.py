from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_apply_configuration import V1beta1ApplyConfiguration
from .v1beta1_json_patch import V1beta1JSONPatch

__all__ = ("V1beta1Mutation",)


class V1beta1Mutation(BaseModel):
    apply_configuration: V1beta1ApplyConfiguration = Field(
        default_factory=lambda: V1beta1ApplyConfiguration(), alias="applyConfiguration"
    )

    json_patch: V1beta1JSONPatch = Field(
        default_factory=lambda: V1beta1JSONPatch(), alias="jsonPatch"
    )

    patch_type: str | None = Field(default_factory=lambda: None, alias="patchType")
