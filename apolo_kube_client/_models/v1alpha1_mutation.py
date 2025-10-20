from pydantic import AliasChoices, BaseModel, Field
from .v1alpha1_apply_configuration import V1alpha1ApplyConfiguration
from .v1alpha1_json_patch import V1alpha1JSONPatch

__all__ = ("V1alpha1Mutation",)


class V1alpha1Mutation(BaseModel):
    apply_configuration: V1alpha1ApplyConfiguration = Field(
        default_factory=lambda: V1alpha1ApplyConfiguration(),
        serialization_alias="applyConfiguration",
        validation_alias=AliasChoices("apply_configuration", "applyConfiguration"),
    )

    json_patch: V1alpha1JSONPatch = Field(
        default_factory=lambda: V1alpha1JSONPatch(),
        serialization_alias="jsonPatch",
        validation_alias=AliasChoices("json_patch", "jsonPatch"),
    )

    patch_type: str | None = Field(
        default=None,
        serialization_alias="patchType",
        validation_alias=AliasChoices("patch_type", "patchType"),
    )
