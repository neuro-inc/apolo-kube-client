from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none


__all__ = ("V1Overhead",)


class V1Overhead(BaseConfiguredModel):
    """Overhead structure represents the resource overhead associated with running a pod."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.node.v1.Overhead"

    pod_fixed: Annotated[
        dict[str, str],
        Field(
            alias="podFixed",
            description="""podFixed represents the fixed resource overhead associated with running a pod.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}
