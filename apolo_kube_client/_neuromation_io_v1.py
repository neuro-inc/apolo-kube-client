from ._attr import _Attr
from ._base_resource import Base, NamespacedResource
from ._crd_models import V1DiskNamingCRD, V1DiskNamingCRDList
from ._models import V1Status
from ._crd_models import (
    V1PersistentBucketCredentialCRD,
    V1PersistentBucketCredentialCRDList,
    V1UserBucketCRD,
    V1UserBucketCRDList,
)


class DiskNamingCRD(NamespacedResource[V1DiskNamingCRD, V1DiskNamingCRDList, V1Status]):  # type: ignore
    query_path = "disknamings"


class UserBucketCRD(NamespacedResource[V1UserBucketCRD, V1UserBucketCRDList, V1Status]):  # type: ignore
    query_path = "userbuckets"


class PersistentBucketCredentialCRD(
    NamespacedResource[
        V1PersistentBucketCredentialCRD, V1PersistentBucketCredentialCRDList, V1Status  # type: ignore
    ]
):
    query_path = "persistentbucketcredentials"


class NeuromationioV1API(Base):
    """
    Neuromation.io v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/neuromation.io/v1"

    disk_naming = _Attr(DiskNamingCRD, group_api_query_path)
    user_bucket = _Attr(UserBucketCRD, group_api_query_path)
    persistent_bucket_credential = _Attr(
        PersistentBucketCredentialCRD, group_api_query_path
    )
