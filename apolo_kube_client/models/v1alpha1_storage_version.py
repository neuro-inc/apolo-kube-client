from pydantic import BaseModel, Field

from .object import object
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_storage_version_status import V1alpha1StorageVersionStatus


class V1alpha1StorageVersion(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: object | None = Field(None, alias="spec")

    status: V1alpha1StorageVersionStatus | None = Field(None, alias="status")
