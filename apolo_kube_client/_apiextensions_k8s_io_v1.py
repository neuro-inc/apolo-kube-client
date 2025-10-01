from kubernetes.client.models import (
    V1CustomResourceDefinition,
    V1CustomResourceDefinitionList,
)

from ._attr import _Attr
from ._base_resource import Base, ClusterScopedResource


class CustomResourceDefinition(
    ClusterScopedResource[
        V1CustomResourceDefinition,
        V1CustomResourceDefinitionList,
        V1CustomResourceDefinition,
    ]
):
    query_path = "customresourcedefinitions"


class ExtensionsK8sV1Api(Base):
    """
    Batch v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/apiextensions.k8s.io/v1"
    crd = _Attr(CustomResourceDefinition, group_api_query_path)
