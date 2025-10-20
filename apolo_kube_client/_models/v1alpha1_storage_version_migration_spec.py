from pydantic import AliasChoices, BaseModel, Field
from .v1alpha1_group_version_resource import V1alpha1GroupVersionResource

__all__ = ("V1alpha1StorageVersionMigrationSpec",)


class V1alpha1StorageVersionMigrationSpec(BaseModel):
    continue_token: str | None = Field(
        default=None,
        serialization_alias="continueToken",
        validation_alias=AliasChoices("continue_token", "continueToken"),
    )

    resource: V1alpha1GroupVersionResource = Field(
        default_factory=lambda: V1alpha1GroupVersionResource()
    )
