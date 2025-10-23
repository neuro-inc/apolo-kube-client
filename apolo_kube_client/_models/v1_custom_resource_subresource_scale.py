from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1CustomResourceSubresourceScale",)


class V1CustomResourceSubresourceScale(BaseModel):
    label_selector_path: str | None = Field(
        default=None,
        serialization_alias="labelSelectorPath",
        validation_alias=AliasChoices("label_selector_path", "labelSelectorPath"),
        exclude_if=_exclude_if,
    )

    spec_replicas_path: str | None = Field(
        default=None,
        serialization_alias="specReplicasPath",
        validation_alias=AliasChoices("spec_replicas_path", "specReplicasPath"),
        exclude_if=_exclude_if,
    )

    status_replicas_path: str | None = Field(
        default=None,
        serialization_alias="statusReplicasPath",
        validation_alias=AliasChoices("status_replicas_path", "statusReplicasPath"),
        exclude_if=_exclude_if,
    )
