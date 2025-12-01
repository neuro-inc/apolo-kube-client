from typing import Annotated, Any

from pydantic import Field

from ._models.base import BaseConfiguredModel, CollectionModel, ResourceModel


class V1DiskNamingCRDSpec(BaseConfiguredModel):
    disk_id: str


class V1DiskNamingCRD(ResourceModel):
    api_version: Annotated[str, Field(alias="apiVersion")] = "neuromation.io/v1"
    kind: str = "DiskNaming"
    spec: V1DiskNamingCRDSpec


class V1DiskNamingCRDList(CollectionModel[V1DiskNamingCRD]):
    api_version: Annotated[str, Field(alias="apiVersion")] = "neuromation.io/v1"
    kind: str = "DiskNamingsList"


class V1UserBucketCRDSpec(BaseConfiguredModel):
    provider_type: str | None
    provider_name: str | None
    created_at: str | None
    public: bool | None
    metadata: dict[str, Any] | None = None
    provider_id: str | None = None
    imported: bool | None = None
    credentials: dict[str, Any] | None = None


class V1UserBucketCRD(ResourceModel):
    api_version: Annotated[str, Field(alias="apiVersion")] = "neuromation.io/v1"
    kind: str = "UserBucket"
    spec: V1UserBucketCRDSpec


class V1UserBucketCRDList(CollectionModel[V1UserBucketCRD]):
    api_version: Annotated[str, Field(alias="apiVersion")] = "neuromation.io/v1"
    kind: str = "UserBucketsList"


class V1PersistentBucketCredentialCRDSpec(BaseConfiguredModel):
    provider_name: str
    provider_type: str
    credentials: dict[str, Any]
    bucket_ids: list[str]
    read_only: bool
    public: bool | None = None


class V1PersistentBucketCredentialCRD(ResourceModel):
    api_version: Annotated[str, Field(alias="apiVersion")] = "neuromation.io/v1"
    kind: str = "PersistentBucketCredential"
    spec: V1PersistentBucketCredentialCRDSpec


class V1PersistentBucketCredentialCRDList(
    CollectionModel[V1PersistentBucketCredentialCRD]
):
    api_version: Annotated[str, Field(alias="apiVersion")] = "neuromation.io/v1"
    kind: str = "PersistentBucketCredentialsList"
