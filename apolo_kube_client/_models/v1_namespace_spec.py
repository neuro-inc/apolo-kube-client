from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none


__all__ = ("V1NamespaceSpec",)


class V1NamespaceSpec(BaseConfiguredModel):
    """NamespaceSpec describes the attributes on a Namespace."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NamespaceSpec"

    finalizers: Annotated[
        list[str],
        Field(
            description="""Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
