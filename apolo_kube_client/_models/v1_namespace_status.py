from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_namespace_condition import V1NamespaceCondition
from pydantic import BeforeValidator

__all__ = ("V1NamespaceStatus",)


class V1NamespaceStatus(BaseModel):
    """NamespaceStatus is information about the current status of a Namespace."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NamespaceStatus"

    conditions: Annotated[
        list[V1NamespaceCondition],
        Field(
            description="""Represents the latest available observations of a namespace's current state.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    phase: Annotated[
        str | None,
        Field(
            description="""Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
