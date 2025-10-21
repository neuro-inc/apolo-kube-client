from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1beta1_apply_configuration import V1beta1ApplyConfiguration
from .v1beta1_json_patch import V1beta1JSONPatch
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1Mutation",)


class V1beta1Mutation(BaseModel):
    apply_configuration: Annotated[
        V1beta1ApplyConfiguration,
        BeforeValidator(_default_if_none(V1beta1ApplyConfiguration)),
    ] = Field(
        default_factory=lambda: V1beta1ApplyConfiguration(),
        serialization_alias="applyConfiguration",
        validation_alias=AliasChoices("apply_configuration", "applyConfiguration"),
    )

    json_patch: Annotated[
        V1beta1JSONPatch, BeforeValidator(_default_if_none(V1beta1JSONPatch))
    ] = Field(
        default_factory=lambda: V1beta1JSONPatch(),
        serialization_alias="jsonPatch",
        validation_alias=AliasChoices("json_patch", "jsonPatch"),
    )

    patch_type: str | None = Field(
        default=None,
        serialization_alias="patchType",
        validation_alias=AliasChoices("patch_type", "patchType"),
    )
