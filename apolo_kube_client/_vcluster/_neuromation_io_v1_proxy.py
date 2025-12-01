from .._crd_models import (
    V1DiskNamingCRD,
    V1DiskNamingCRDList,
    V1PersistentBucketCredentialCRD,
    V1PersistentBucketCredentialCRDList,
    V1UserBucketCRD,
    V1UserBucketCRDList,
)
from .._models import V1Status
from .._neuromation_io_v1 import (
    DiskNamingCRD,
    NeuromationioV1API,
    PersistentBucketCredentialCRD,
    UserBucketCRD,
)
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy


class DiskNamingCRDProxy(
    NamespacedResourceProxy[
        V1DiskNamingCRD, V1DiskNamingCRDList, V1Status, DiskNamingCRD
    ]
):
    pass


class UserBucketCRDProxy(
    NamespacedResourceProxy[
        V1UserBucketCRD, V1UserBucketCRDList, V1Status, UserBucketCRD
    ]
):
    pass


class PersistentBucketCredentialCRDProxy(
    NamespacedResourceProxy[
        V1PersistentBucketCredentialCRD,
        V1PersistentBucketCredentialCRDList,
        V1Status,
        PersistentBucketCredentialCRD,
    ]
):
    pass


class NeuromationioV1APIProxy(BaseProxy[NeuromationioV1API]):
    """
    Neuromation.io v1 API wrapper for Kubernetes.
    """

    @attr(DiskNamingCRDProxy)
    def disk_naming(self) -> DiskNamingCRD:
        return self._origin.disk_naming

    @attr(UserBucketCRDProxy)
    def user_bucket(self) -> UserBucketCRD:
        return self._origin.user_bucket

    @attr(PersistentBucketCredentialCRDProxy)
    def persistent_bucket_credential(self) -> PersistentBucketCredentialCRD:
        return self._origin.persistent_bucket_credential
