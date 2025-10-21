from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1alpha1_group_version_resource import V1alpha1GroupVersionResource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1StorageVersionMigrationSpec",)


class V1alpha1StorageVersionMigrationSpec(BaseModel):
    continue_token: str | None = Field(
        default=None,
        serialization_alias="continueToken",
        validation_alias=AliasChoices("continue_token", "continueToken"),
    )

    resource: Annotated[
        V1alpha1GroupVersionResource,
        BeforeValidator(_default_if_none(V1alpha1GroupVersionResource)),
    ] = Field(default_factory=lambda: V1alpha1GroupVersionResource())
