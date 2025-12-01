from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base import CollectionModel
from .utils import KubeMeta, _default_if_none
from .v1_list_meta import V1ListMeta
from .v1_service_account import V1ServiceAccount


__all__ = ("V1ServiceAccountList",)


class V1ServiceAccountList(CollectionModel[V1ServiceAccount]):
    """ServiceAccountList is a list of ServiceAccount objects"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ServiceAccountList"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="", kind="ServiceAccountList", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "v1"

    items: Annotated[
        list[V1ServiceAccount],
        Field(
            description="""List of ServiceAccounts. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/"""
        ),
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "ServiceAccountList"

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
