from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha1_apply_configuration import V1alpha1ApplyConfiguration
from .v1alpha1_json_patch import V1alpha1JSONPatch

__all__ = ("V1alpha1Mutation",)


class V1alpha1Mutation(BaseModel):
    apply_configuration: V1alpha1ApplyConfiguration = Field(
        default_factory=lambda: V1alpha1ApplyConfiguration(), alias="applyConfiguration"
    )

    json_patch: V1alpha1JSONPatch = Field(
        default_factory=lambda: V1alpha1JSONPatch(), alias="jsonPatch"
    )

    patch_type: str | None = Field(default_factory=lambda: None, alias="patchType")
