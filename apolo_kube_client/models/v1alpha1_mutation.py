from pydantic import BaseModel, Field

from .v1alpha1_apply_configuration import V1alpha1ApplyConfiguration
from .v1alpha1_j_s_o_n_patch import V1alpha1JSONPatch


class V1alpha1Mutation(BaseModel):
    apply_configuration: V1alpha1ApplyConfiguration | None = Field(
        None, alias="applyConfiguration"
    )

    json_patch: V1alpha1JSONPatch | None = Field(None, alias="jsonPatch")

    patch_type: str | None = Field(None, alias="patchType")
