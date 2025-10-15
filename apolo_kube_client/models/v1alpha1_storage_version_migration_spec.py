from pydantic import BaseModel, Field

from .v1alpha1_group_version_resource import V1alpha1GroupVersionResource


class V1alpha1StorageVersionMigrationSpec(BaseModel):
    continue_token: str | None = Field(None, alias="continueToken")

    resource: V1alpha1GroupVersionResource | None = Field(None, alias="resource")
