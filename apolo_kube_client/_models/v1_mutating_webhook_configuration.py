from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base import ResourceModel
from .utils import KubeMeta, _collection_if_none, _default_if_none
from .v1_mutating_webhook import V1MutatingWebhook
from .v1_object_meta import V1ObjectMeta


__all__ = ("V1MutatingWebhookConfiguration",)


class V1MutatingWebhookConfiguration(ResourceModel):
    """MutatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and may change the object."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.MutatingWebhookConfiguration"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="admissionregistration.k8s.io",
        kind="MutatingWebhookConfiguration",
        version="v1",
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "admissionregistration.k8s.io/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "MutatingWebhookConfiguration"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    webhooks: Annotated[
        list[V1MutatingWebhook],
        Field(
            description="""Webhooks is a list of webhooks and the affected resources and operations.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
