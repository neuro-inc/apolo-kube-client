from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha1_storage_version import V1alpha1StorageVersion


class V1alpha1StorageVersionList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha1StorageVersion] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
